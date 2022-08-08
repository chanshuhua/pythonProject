import os

import pymysql
import logging

import yaml


class DBOperateAction(object):
    def __init__(self,dbhost,dbacount,dbpasswd,dbname,dbport='3306',charset='utf-8'):
        '''
        初始化
        :param dbhost:  数据库域名/Ip地址
        :param dbacount: 数据库登录用户名
        :param dbpasswd: 数据库登录密码
        :param dbname: 数据库名称
        :param dbport: 数据库端口
        :param charset: 默认字符格式
        '''
        # '172.18.163.228','root','uWXf87plmQGz8zMM','see_management_4'
        self.dbhost = dbhost
        self.dbacount = dbacount
        self.dbpasswd = dbpasswd
        self.dbname = dbname
        self.dbport = dbport
        self.charset = charset

        self.db_conn = object #全局数据库对象
        self.db_conn_cursor = object  #全局数据库游标对象

    def connect(self,autocommit=False):
        '''
        连接数据库
        :param flag:
        :param query:
        :param autocommit:
        :return:
        '''
        # 1、连接数据库
        try:
            self.db_conn = pymysql.connect(
                host=self.dbhost,
                user=self.dbacount,
                password=self.dbpasswd,
                db=self.dbname,
                charset=self.charset,
                autocommit=autocommit  # 是否自动提交
            )
            # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
            # 2、 创建游标对象
            self.db_conn_cursor = self.db_conn.cursor()
            return True
        except pymysql.OperationalError:
            logging.error("Connect to {} Failed".format(self.dbhost))
            logging.exception("Failed_logging:")
            return False

    def re_connect(self):
        '''
        重连机制
        :return:
        '''
        logging.error("reconnecting")
        try:
            res = self.connect()
            if not res:
                # 重连两遍
                self.connect()
        except pymysql.OperationalError:
            logging.error("Connect to {} ERROR".format(self.dbhost))
            logging.exception("Failed_logging:")

    def close(self):
        '''
        关闭连接
        :return:
        '''
        # 4、关闭游标
        self.db_conn_cursor.close()
        # 5、关闭数据库
        self.db_conn.close()

    def cursor_index0(self):
        '''
        光标恢复首行
        :return:
        '''
        self.db_conn_cursor.scroll(0, mode='absolute')  # 设置之后，光标相对于首行没有任何变化，所以打印的结果为第一行数据

    def cursor_preindex(self):
        '''
        光标指向上一行
        :return:
        '''
        self.db_conn_cursor.scroll(-1, mode='relative')

    def index(self,index):
        if index == 0:
            self.cursor_index0()
        elif index == 1:
            self.cursor_preindex()

    def getOnefetch(self,sql,index=0):
        '''
        获取下一行数据，第一次为首行
        :param sql:
        :return:
        '''
        try:
            logging.info("Execute sql: "+ sql)
            #  sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            #  cursor.execute(sql, ('webmaster@python.org',))
            self.db_conn_cursor.execute(sql)
            self.db_conn.commit()
            data = self.db_conn_cursor.fetchone()
            self.index(index)
            return data
        except pymysql.OperationalError:
            logging.error("Searching {} Failed".format(sql))

    def getAllfetch(self,sql):
        '''
        查询全部结果
        :param sql:查询全部结果的sql语句
        :return:
        '''
        # 3、查询全部数据
        try:
            logging.info("Execute sql: "+ sql)
            #  sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            #  cursor.execute(sql, ('webmaster@python.org',))
            self.db_conn_cursor.execute(sql)
            self.db_conn.commit()
            data = self.db_conn_cursor.fetchall_unbuffered() #非缓存的全部结果
            # self.close()
            return data
        except pymysql.OperationalError:
            logging.error("Searching {} Failed".format(sql))

    def getManycfetch(self,sql,query,index=0):
        '''
        查询many行数的结果
        :param sql:
        :return:
        '''
        try:
            logging.info("Execute sql: "+ sql)
            #  sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            #  cursor.execute(sql, ('webmaster@python.org',))
            self.db_conn_cursor.execute(sql)
            self.db_conn.commit()
            data = self.db_conn_cursor.fetmany(query=query)
            self.index(index)
            return data
        except pymysql.OperationalError:
            logging.error("Searching {} Failed".format(sql))


class DBOperationfile(object):
    '''
    查找文件（分库分表）
    '''
    def __init__(self):
        self.datapath = ''

    def read_dbsql_byfilename(self,filename,method=0,index=0):
        rootpath = os.path.dirname(os.path.abspath(__file__)).split('commom')[0].replace('\\','/')
        self.datapath = os.path.join(rootpath,'test/',filename)
        if method == 0:
            value = self.get_sql_byyaml()
        else:
            value = self.get_sql_byindex(index)
        print(value)
        return value

    def get_sql_byyaml(self):
        '''
        :param index: 数据库存储可变参数的sql
        :param args: 查询参数
        :return:
        '''
        sql = ''
        with open(self.datapath, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            for i in value['sql']:
                sql += str(i)+ ' ' + str(value['sql'][i]) + ' '
            return sql

    def get_sql_byindex(self,index):
        '''
        :param index: 数据库存储下标
        :param args: 查询参数
        :return:
        '''
        sql = ''
        with open(self.datapath, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)['sqls']
            sql = value[index]
            return sql

if __name__ == '__main__':
        # search_sql = 'select id from '
       # DBOperationfile().read_dbsql_byfilename("sql_see_management_byname.yaml")
       # DBOperationfile().read_dbsql_byfilename("sql_see_management_byindex.yaml",method=1,index=0)

        for i in range(1,10):
            for j in range(1,i+1):
                print("%s x %s = %s" %(j,i,j*i),end='\t')
            print('\n')

        # chine = 'shd'
        # print("%s" %chine)

        lst = [1,2,3,4,2,3,4,2,3]
        lstset = set(lst)
        print(list[lstset])