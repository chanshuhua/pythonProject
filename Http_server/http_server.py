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


# 思路：
# 方法文档 https://docs.python.org/zh-cn/3/library/http.server.html
#  父类：BaseHTTPRequestHandler -》 TCP Server -》 HTTP Server

# 查看 Http请求在网络中是如何转发的



port = 8000
server_address = ('127.0.0.1',port)

class Handler(BaseHTTPRequestHandler):
    '''
    BaseHTTPRequestHandler 为定义简单的http server
    定义 get post请求方法
    '''
    def do_HEAD(self):
        # return self.headers
        pass

    def do_GET(self):
        self.send_response(200,'get')  # 服务端发送成功后获取的response
        self.send_header('Content-Type','application/json') # 发送给客户端的header包含内容
        self.end_headers()  # close headers
        # self.send_error(500)

        message = {'code':200,'message':'get request SUCCESS'}   # 返回给客户端的内容
        message_bytes = json.dumps(message).encode()
        self.wfile.write(message_bytes)  # 输出流至客户端

        # 解析客户端过来的请求头、内容..
        print(self.headers)

        # 获取请求体url...
        url = 'http://' + server_address[0] + ':' + str(server_address[1]) + self.path
        print(url)

        # 如何获取url中的请求参数 params and value
        print("get request params: {}".format(self.path)) # 解析get请求需要请求的参数！！

        # 对请求参数做后面的处理



    def do_POST(self):
        self.send_response(200,'post')  # 服务端向客户端发送状态码和参数内容
        self.send_header('Content-Type', 'application/json') #  服务端向客户端发送请求格式
        self.end_headers()
        # self.send_error(500)


        # 服务端返回内容到客户端
        # 输出流至客户端
        req_data_bytes = self.rfile.read(int(self.headers['content-length']))  # 获取客户端发送体的Content-Type 内容

        # message = {'code': 200, 'message': 'post request SUCCESS' }  # 返回给客户端的内容
        # print(type(message))
        # message_bytes = json.dumps(req_data_bytes).encode()
        # print(message_bytes)
        self.wfile.write(req_data_bytes)  # 输出流至客户端

        # 解析客户端过来的请求头、内容..
        print(self.headers)

        # print("Postman-Token:{}".format(self.headers['Postman-Token'])) # 可获取客户端的发送的鉴权信息
        # print(self.headers["Cookie"])

        # 获取请求体url...
        url = 'http://' + server_address[0] + ':' + str(server_address[1]) + self.path
        print(url)

        # # 获取请求内容
        # req_data_bytes = self.rfile.read(int(self.headers['content-length']))  # 获取客户端发送体的Content-Type 内容
        req_data = json.loads(req_data_bytes)  # bytes->json 将post请求中的输入流拦截
        print(self.path)
        print("请求体：{}".format(req_data))

        # 对请求参数做处理


with HTTPServer(server_address,Handler) as httpd:
    try:
        print("-------------Serving in port", port)
        httpd.serve_forever()

    except KeyboardInterrupt or SyntaxError:
        httpd.send_error(500)
        httpd.log_error()
        httpd.socket.close()



