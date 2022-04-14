# coding=gbk
import redis
import traceback
from rediscluster import RedisCluster

import paramiko

redis_basis_conn = [
    {'host': '172.18.163.240', 'port': 47001},
    {'host': '172.18.163.240', 'port': 47002},
    {'host': '172.18.163.240', 'port': 47003},
    {'host': '172.18.163.240', 'port': 47004},
    {'host': '172.18.163.240', 'port': 47005},
    {'host': '172.18.163.240', 'port': 47006}
    ]
password = 'AhspHJ2l0ychcves'


class Redis_cluster():
    def __init__(self,startup_nodes,password):
        self.startup_nodes = startup_nodes
        self.password = password

    def conn(self):
        try:
            r = RedisCluster(startup_nodes=self.startup_nodes, decode_responses=True, password=self.password)
            print("connect success!")
            return r
        except Exception as e:
            print("connect fail!")
            traceback.print_exc()
            return e



if __name__ == '__main__':

    r = Redis_cluster(redis_basis_conn,password).conn()
    print(str(r))
    assert ('RedisCluster' in str(r))

    # r.set("new","one")
    # print(r.get('new'))