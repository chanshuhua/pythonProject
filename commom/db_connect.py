import pymysql

class Database(object):
    def __init__(self):
        self.host = '172.18.163.228'
        self.user = 'root'
        self.password = 'uWXf87plmQGz8zMM'
        self.db = 'see_management_4'

    def db_conn(self,flag,query,autocommit=False):
        # 1、链接数据库
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8',
            autocommit=autocommit  # 是否自动提交
        )

        # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
        # 2、 创建游标对象
        cur = conn.cursor()
        # 3. 对于数据库进行增删改查
        # 对数据库进行查询
        if flag == 'search':
            cur.execute(query=query)
            data = cur.fetchone()
            return data
        else:
            return -1

        # 4、关闭数据库
        conn.close()


if __name__ == '__main__':
        search_sql = 'select id from '
        data = Database().db_conn('search',search_sql,True)
        print(data)