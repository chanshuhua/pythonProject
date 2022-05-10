# coding=gbk
import json
from base64 import encode
from http.server import HTTPServer,BaseHTTPRequestHandler
import socketserver

# port = 8000
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("",port),Handler) as httpd:
#     print("serving in port ",port)
#     httpd.serve_forever()


# ˼·��
# �����ĵ� https://docs.python.org/zh-cn/3/library/http.server.html
#  ���ࣺBaseHTTPRequestHandler -�� TCP Server -�� HTTP Server

# �鿴 Http�����������������ת����



port = 8000
server_address = ('127.0.0.1',port)

class Handler(BaseHTTPRequestHandler):
    '''
    BaseHTTPRequestHandler Ϊ����򵥵�http server
    ���� get post���󷽷�
    '''
    def do_HEAD(self):
        # return self.headers
        pass

    def do_GET(self):
        self.send_response(200,'get')  # ����˷��ͳɹ����ȡ��response
        self.send_header('Content-Type','application/json') # ���͸��ͻ��˵�header��������
        self.end_headers()  # close headers
        # self.send_error(500)

        message = {'code':200,'message':'get request SUCCESS'}   # ���ظ��ͻ��˵�����
        message_bytes = json.dumps(message).encode()
        self.wfile.write(message_bytes)  # ��������ͻ���

        # �����ͻ��˹���������ͷ������..
        print(self.headers)

        # ��ȡ������url...
        url = 'http://' + server_address[0] + ':' + str(server_address[1]) + self.path
        print(url)

        # ��λ�ȡurl�е�������� params and value
        print("get request params: {}".format(self.path)) # ����get������Ҫ����Ĳ�������

        # ���������������Ĵ���



    def do_POST(self):
        self.send_response(200,'post')  # �������ͻ��˷���״̬��Ͳ�������
        self.send_header('Content-Type', 'application/json') #  �������ͻ��˷��������ʽ
        self.end_headers()
        # self.send_error(500)


        # ����˷������ݵ��ͻ���
        # ��������ͻ���
        req_data_bytes = self.rfile.read(int(self.headers['content-length']))  # ��ȡ�ͻ��˷������Content-Type ����

        # message = {'code': 200, 'message': 'post request SUCCESS' }  # ���ظ��ͻ��˵�����
        # print(type(message))
        # message_bytes = json.dumps(req_data_bytes).encode()
        # print(message_bytes)
        self.wfile.write(req_data_bytes)  # ��������ͻ���

        # �����ͻ��˹���������ͷ������..
        print(self.headers)

        # print("Postman-Token:{}".format(self.headers['Postman-Token'])) # �ɻ�ȡ�ͻ��˵ķ��͵ļ�Ȩ��Ϣ
        # print(self.headers["Cookie"])

        # ��ȡ������url...
        url = 'http://' + server_address[0] + ':' + str(server_address[1]) + self.path
        print(url)

        # # ��ȡ��������
        # req_data_bytes = self.rfile.read(int(self.headers['content-length']))  # ��ȡ�ͻ��˷������Content-Type ����
        req_data = json.loads(req_data_bytes)  # bytes->json ��post�����е�����������
        print(self.path)
        print("�����壺{}".format(req_data))

        # ���������������


with HTTPServer(server_address,Handler) as httpd:
    try:
        print("-------------Serving in port", port)
        httpd.serve_forever()

    except KeyboardInterrupt or SyntaxError:
        httpd.send_error(500)
        httpd.log_error()
        httpd.socket.close()



