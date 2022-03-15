from http.server import BaseHTTPRequestHandler, HTTPServer
import jsonpath

class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello,web!</p>
        </body>
        </html>
    '''
    callback = []


    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        print(server.get_request())
        self.send_header("Content-Length", str(len(self.content)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

    def do_post(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()




if __name__ == '__main__':
    # serverAddress = ('', 8080)
    # server = HTTPServer(serverAddress, RequestHandler)
    # server.serve_forever()

    # a = [1,2,3]
    # del a[1]
    # print(a)
    # print(len(a))
    # for i in range(len(a)):
    #     print(i)
    #     del a[i]
    # print(a)
    ruleItems_used = ['语义-其他坐席', '语义-与圆梦共享']
    ruleItems = [{'criticalType': 2, 'id': 55, 'name': '语义-其他坐席', 'parentId': None, 'parentName': None, 'type': 1}, {'criticalType': 1, 'id': 56, 'name': '语义-总费用提示', 'parentId': None, 'parentName': None, 'type': 1}, {'criticalType': 1, 'id': 57, 'name': '语义-提示违约金', 'parentId': None, 'parentName': None, 'type': 1}, {'criticalType': 1, 'id': 58, 'name': '语义-提示录音', 'parentId': None, 'parentName': None, 'type': 1}, {'criticalType': 1, 'id': 60, 'name': '语义-开场白修改开场白名称', 'parentId': None, 'parentName': None, 'type': 1}, {'criticalType': 1, 'id': 158, 'name': '语义-与圆梦共享', 'parentId': None, 'parentName': None, 'type': 1}]
    ruleItems_avail = []
    save_parm_text = jsonpath.jsonpath(ruleItems, '$..' + 'name')
    # for i in range(len(ruleItems)):
    #     save_parm_text = str(save_parm_text)
    #     print(i)
    #     print(save_parm_text)
    #     if i not in save_parm_text:
    #         ruleItems_avail.append(i)
    # print(ruleItems_avail)
    #     for j in ruleItems_used:
    #         if ruleItems[i]['name'] !=


    # for index, value in enumerate(b):
    #     for i in a:
    #         if value['name'] == i:
    #             print('in')
    #             b.pop(index)
    #             print(b)
    #         else:
    #             print('notin')
    # #
    # # print(b)


    # for j in range(len(ruleItems)):
    #     flag = False
    #     for i in range(len(ruleItems_used)):
    #         print(ruleItems[j])
    #         print(ruleItems_used[i])
    #         if ruleItems_used[i] == ruleItems[j]["name"]:
    #             flag = True
    #     if not flag:
    #         ruleItems_avail.append(ruleItems[j])
# 2
#     for j in range(len(ruleItems)):
#
#         for i in range(len(ruleItems_used)):
#             print(ruleItems[j])
#             print(ruleItems_used[i])
#             if ruleItems_used[i] = ruleItems[j]["name"]:
#                 break
#
#             ruleItems_avail.append(ruleItems[j])

    # a = '9'
    # if a:
    #     print('t')
    # elif not a:
    #     print('f')
