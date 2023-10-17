import socket
import time
import hashlib
import re


class CheckRtsp():
    def __init__(self):
        pass

    # 用于Digest认证方式时生成response的值
    def gen_response_value(self, url, public_method, realm, nonce, username, password):
        frist_pre_md5_value = hashlib.md5((username + ':' + realm + ':' + password).encode()).hexdigest()
        first_post_md5_value = hashlib.md5((public_method + ':' + url).encode()).hexdigest()
        response_value = hashlib.md5(
            (frist_pre_md5_value + ':' + nonce + ':' + first_post_md5_value).encode()).hexdigest()
        return response_value

    # 执行一次完整的rtsp播放请求，OPTIONS/DESCRIBE/SETUP/PLAY/GET PARAMETER/TEARDOWN，如果某个请求不正确则中止。
    # 此检测检测到第二个DESCRIBE请求后即可判断视频流是否在线
    def check_rtsp(self, rtsp_stream):
        pattern = r"rtsp://(.*):(.*)@(.*):\d+"
        match = re.match(pattern, rtsp_stream)
        if match:
            username = match.group(1)
            password = match.group(2)
            ip = match.group(3)
        else:
            print("未能提取用户名、密码和IP地址。")
            return False
        try:
            self.socket_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_send.settimeout(0.06)  # 0.04开始可以检测到所有的视频在线，低于这个值的话会出现在线视频检测不到
            self.socket_send.connect((ip, 554))

            # OPTIONS 请求
            print('now start to check options operation')
            header_head = 'OPTIONS '
            header_cseq = ' RTSP/1.0\r\nCSeq: 2\r\n'
            header_useragent = 'User-Agent: LibVLC/3.0.2 (LIVE555 Streaming Media v2016.11.28)\r\n\r\n'
            str_options_header = header_head + rtsp_stream + header_cseq + header_useragent
            self.socket_send.send(str_options_header.encode())
            msg_recv = self.socket_send.recv(1024).decode()
            if '200 OK' in msg_recv:
                print('OPTIONS request is OK')
                return True
            else:
                print('OPTIONS request is BAD')

            # 第一、二次的describe
            str_describe_1 = 'DESCRIBE '
            str_describe_cseq = ' RTSP/1.0\r\nCSeq: 3\r\n'
            str_describe_useragent = 'User-Agent: LibVLC/3.0.2 (LIVE555 Streaming Media v2016.11.28)\r\nAccept: application/sdp\r\n\r\n'
            str_describe_header = str_describe_1 + rtsp_stream + str_describe_cseq + str_describe_useragent
            self.socket_send.send(str_describe_header.encode())
            msg_recv = self.socket_send.recv(1024).decode()
            if msg_recv.find('401 Unauthorized') == -1 & False:
                msg_recv_dict = msg_recv.split('\r\n')
                print('first DESCRIBE request occur error: ')
                print(msg_recv_dict[0])
            else:
                print('first DESCRIBE is ok,now we will execute second DESCRIBE for auth')
                realm_pos = msg_recv.find('realm')
                realm_value_begin_pos = msg_recv.find('"', realm_pos) + 1
                realm_value_end_pos = msg_recv.find('"', realm_pos + 8)
                realm_value = msg_recv[realm_value_begin_pos:realm_value_end_pos]
                nonce_pos = msg_recv.find('nonce')
                nonce_value_begin_pos = msg_recv.find('"', nonce_pos) + 1
                nonce_value_end_pos = msg_recv.find('"', nonce_pos + 8)
                nonce_value = msg_recv[nonce_value_begin_pos:nonce_value_end_pos]
                str_describe_cseq = ' RTSP/1.0\r\nCSeq: 4\r\n'
                response_value = self.gen_response_value(rtsp_stream, 'DESCRIBE', realm_value, nonce_value, username,
                                                         password)
                digest_options_header = 'Authorization: Digest username="' + username + '", realm="' + realm_value + '", nonce="' + nonce_value + '", uri="' + rtsp_stream + '", response="' + response_value + '"\r\n'
                str_describe_auth_header = str_describe_1 + rtsp_stream + str_describe_cseq + digest_options_header + str_describe_useragent
                # print('describe2:{}'.format(str_describe_auth_header))
                self.socket_send.send(str_describe_auth_header.encode())
                msg_recv = self.socket_send.recv(1024).decode()
                if msg_recv.find('200 OK') == -1:
                    msg_recv_dict = msg_recv.split('\r\n')
                    print('second DESCRIBE request occur error: {}'.format(msg_recv_dict[0]))
                    return False
                else:
                    print('DESCRIBE request is OK')
                    return True
        except Exception as e:
            print("连接失败:{}".format(e))
            return False


if __name__ == '__main__':
    rtsp_stream = 'rtsp://admin:password01!@192.168.188.21:554/Streaming/Channels/501'
    # rtsp_stream = 'rtsp://admin:a1234567@192.168.188.64:554/h264/ch33/main/av_stream'
    rtsp_stream_no = 'rtsp://admin:a1234567@192.168.188.18:554/h264/ch33/main/av_stream'
    rtsp_streams = []
    for i in range(50):
        rtsp_streams.append(rtsp_stream)
        rtsp_streams.append(rtsp_stream_no)
    star_time = time.time()
    # 1.创建
    rtsp_client = CheckRtsp()
    sum = 0
    for rtsp_stream in rtsp_streams:
        # 2.检测
        ret = rtsp_client.check_rtsp(rtsp_stream)
        if ret:
            sum += 1
    print('有{}个视频在线'.format(sum))
    end_time = time.time()
    print("总用时：", end_time - star_time)
