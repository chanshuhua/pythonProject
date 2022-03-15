import json
from threading import Thread
import asyncio
from urllib.parse import unquote
import requests
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado import netutil
import logging

# from code.tests.interface.common.read_testcase import getParam
# from code.tests.interface.common.server_conf import *
# from code.tests.interface.common.Server_interface import Server_Interface
# from code.tests.interface.common.stop_Thread import Stop_Thread
# from code.tests.interface.common.server_lock import file
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("./code/logs/learn_http_server.log",encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class getSetting_Handler(tornado.web.RequestHandler):
    def initialize(self, get_para, type, asrbitrate,ttsbitrate,replaytimeout,speechtimeout, schedule_ip, http_ip):
        self.setting_get=get_para
        self.setting_get["data"]["asr"]["scheduleUrl"] = schedule_ip
        self.setting_get["data"]["tts"]["scheduleUrl"] = schedule_ip
        self.setting_get["data"]["asr"]["bitrate"] = asrbitrate
        self.setting_get["data"]["tts"]["bitrate"] = ttsbitrate
        self.setting_get["data"]["replaytimeout"] = replaytimeout
        self.setting_get["data"]["speechtimeout"] = speechtimeout
        self.setting_get["data"]["strategy"]["name"] = type
        self.setting_get["data"]["bot"]["node_url"] = http_ip + "/learn-app/api/v1/voice/sessions/{session_id}/node"
        self.setting_get["data"]["bot"]["session_url"] = http_ip + "/learn-app/api/v1/voice/sessions/{session_id}"

    def get(self, sessionid):
        print("访问setting接口的ip：", self.request.remote_ip)
        self.write(self.setting_get)
        logger.info("——-----------获取全局参数get ")
        logger.info(sessionid)

class next_node_Handler(tornado.web.RequestHandler):
    def initialize(self,post_para,get_para,end_node):
        self.next_node_post = post_para
        self.next_node_get = get_para
        self.end_node_get = end_node
    def get(self,sessionid):#拉取下一轮节点 get
        node_num = dict_node_num.setdefault(sessionid, 0)
        print("拉取节点", node_num +1, sessionid)
        if node_num<len(self.next_node_get) and node_num>=0:
            node = {'code': 0, 'msg': 'success','data': {'customerText': "", 'nodeType': "", 'nodeindex': "", 'recordBlob': ""}}
            node["data"].update(customerText=self.next_node_get[node_num]['text'],
                                nodeType=self.next_node_get[node_num]['type'],
                                nodeindex=self.next_node_get[node_num]['nodeindex'],
                                recordBlob=self.next_node_get[node_num]['file'])  # 注意title不用加引号
            logger.info(node)
            self.write(node)
            node_num += 1
            dict_node_num[sessionid] = node_num
        else:
            self.write(self.end_node_get)
            print("拉取空节点",node_num+1)
        logger.info("——-----------拉取下一轮节点get: "+str(node_num))

    def post(self,sessionid):#通知节点信息 post
        request=self.request.body.decode('utf-8')
        request = unquote(request)
        request = json.loads(request)
        logger.info(request)
        self.write(self.next_node_post)
        logger.info("——-----------通知节点信息post")
        if len(request["recordUrl"])!=0:
            recordUrl = request["recordUrl"]
            print(request)
            assert_rerecord(recordUrl)
            print("断言通过————通知节点信息的请求recordUrl访问成功")

class undo_node_Handler(tornado.web.RequestHandler):
    def initialize(self,get_para,end_node):
        self.next_node_get = get_para
        self.end_node_get=end_node
    def post(self,sessionid):
        dict_node_num.setdefault(sessionid, 0)
        dict_node_num[sessionid] = dict_node_num[sessionid] - 1
        self.write({"code":0,"msg": "undo_post responses"})
        print("——-----------撤回当前节点post")
        logger.info("——-----------撤回当前节点post")

class postSession_Handler(tornado.web.RequestHandler):
    def initialize(self,post_para):
        self.push_post = post_para
    def post(self,sessionid):#推送会话信息 post
        self.write(self.push_post)
        r = self.request.body.decode('utf-8')
        r = unquote(r)#url解码
        request = json.loads(r)
        recordUrl=request["recordUrl"]
        assert_rerecord(recordUrl)
        print(request)
        print("断言通过————推送会话信息的请求recordUrl访问成功")


def assert_rerecord(recordUrl):#请求recordUrl
    logger.info(recordUrl)
    r = requests.get(recordUrl, headers={'Content-Type': 'application/json'}, verify=False)
    assert r.status_code==200
    assert type(r.content) == bytes

def http_app(s,http_port,conf,schedule_port):
    http_conf = Server_Conf().get_read_conf("/learn/learn_server_conf.yaml")  # 基本配置由文件读出
    docker_ip = Server_Conf().get_server_ip()
    schedule_ip = docker_ip + ":" + str(schedule_port)
    http_ip = "http://" + docker_ip + ":" + str(http_port)
    global dict_node_num
    dict_node_num = {}
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())  # 事件循环
        # 建立路由表
        application = tornado.web.Application(handlers=[
            (r"/learn-app/api/v1/voice/sessions/(?P<sessionid>.+)/setting", getSetting_Handler,dict(get_para=http_conf["setting_get"],type=conf["setting"]["type"],asrbitrate=conf["setting"]["asrbitrate"],ttsbitrate=conf["setting"]["ttsbitrate"],replaytimeout=conf["setting"]["replaytimeout"],speechtimeout=conf["setting"]["speechtimeout"],schedule_ip=schedule_ip,http_ip=http_ip)),
            (r"/learn-app/api/v1/voice/sessions/(?P<sessionid>.+)/node", next_node_Handler,dict(post_para=http_conf["next_node_post"],get_para=conf["nodes"],end_node=http_conf["end_node"])),
            (r"/learn-app/api/v1/voice/sessions/(?P<sessionid>.+)/node/undo", undo_node_Handler,dict(get_para=conf["nodes"],end_node=http_conf["end_node"])),
            (r"/learn-app/api/v1/voice/sessions/(?P<sessionid>.+)", postSession_Handler,dict(post_para=http_conf["push_post"])),
            ], debug=True)
        server = tornado.httpserver.HTTPServer(application)  # 创建http服务器
        server.add_sockets(s)
        logger.info("http_server start ！")
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        print('启动learn_http服务发生异常:', repr(e),str(http_port))
        logger.info("----error:报错详情：" + repr(e) + "___" + str(http_port))
        assert False



class Learn_Server(Server_Interface):
    def __init__(self,conf,schedule_port):
        # 产生随机端口，启动服务
        fcntl.flock(file.fileno(), fcntl.LOCK_EX)
        logger.info("http_server 加锁")
        s = tornado.netutil.bind_sockets(0)
        self.http_port = s[0].getsockname()[1]
        logger.info("--lock http_server port"+str(self.http_port))
        self.server = Thread(target=http_app, args=(s, self.http_port, conf, schedule_port))
        self.server.start()
        logger.info("--lock http_server 解锁" + str(self.http_port))
        fcntl.flock(file.fileno(), fcntl.LOCK_UN)


    def get_port(self):
        return self.http_port

    def close(self):
        Stop_Thread().stop(self.server)
        print("停止线程")



if __name__ == "__main__":
    def allserver_test(p):
        time.sleep(3)
        ip = 'http://localhost:' + str(p)  #
        sessionid = '1380364258587611136'
        header = {'Content-Type': 'application/json', 'encoding': 'utf-8'}
        url1 = ip + '/learn-app/api/v1/voice/sessions/' + sessionid + '/setting'  # 拉取全局参数 get
        url2 = ip + '/learn-app/api/v1/voice/sessions/' + sessionid + '/node'  # 拉取下一轮节点 get
        url3 = ip + '/learn-app/api/v1/voice/sessions/' + sessionid + '/node/undo'  # 撤回当前节点 get---post
        url4 = ip + '/learn-app/api/v1/voice/sessions/' + sessionid + '/node'  # 通知节点信息 post
        url5 = ip + '/learn-app/api/v1/voice/sessions/' + sessionid  # 推送会话信息 post
        data41 = '{"nodeType": 1, "text": "是的是的", "timestamp": 1625812848627, "speed": 8, "status": 1, "recordUrl": "","startTime": 1540, "endTime": 1790, "nodeindex": 2}'
        data4 = '{"nodeType":1,"text":"是的是的","timestamp":1625812849659,"speed":0,"status":2,"recordUrl":"http://172.18.164.131:38091/api/v1/recorder/audios/9255cb55e08011eba833b886878c20f8_2?type=1&start_time_ms=3502&end_time_ms=8002","startTime":1540,"endTime":1790,"nodeindex":2}'
        data5 = '{"recordUrl":"http://172.18.164.131:38091/api/v1/recorder/audios/7851faf6dfe811eb8614b886878c20f8_2?type=0&start_time_ms=0&end_time_ms=8889","timeCost":8889}'
        data4 = data4.encode("utf-8").decode("latin1")  # post数据携带中文 编码成bytes（utf-8）格式再解码为latin1
        data41 = data41.encode("utf-8").decode("latin1")  # url为空
        url_list_get = [url1,url2, url2, url2,url2, url2]
        for url in url_list_get:
            print("自测接口~~~~~~~~~~~~~~~~~~~~", url)
            r = requests.get(url, headers=header, verify=False)
            print("自测返回~~~~~~~~~~~~~~~~~~~~",r.content.decode("utf-8"))
        # url3,
        url_list_post = [{"url": url4, "data": data4}, {"url": url4, "data": data41}, {"url": url5, "data": data5}]  # ,
        for p in url_list_post:
            print("自测接口~~~~~~~~~~~~~~~~~~~~", p["url"])
            r = requests.post(p["url"], headers=header, data=p["data"], verify=False)
            print("自测返回~~~~~~~~~~~~~~~~~~~~",r.content.decode("utf-8"))
    case=getParam().cases_under_path("learn/faq_case")
    conf=case[1]["tests"]["params"]["http"]
    learn_server=Learn_Server(conf,2003)
    port=learn_server.get_port()
    allserver_test(port)
    learn_server.close()
    print(port)
    allserver_test(port)











