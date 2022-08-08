import pymysql
import api
# 初始化数据库
# 创建用户数据表，用户数据表收录用户名，密码，用户id
def MakeDatabase():
    conn = pymysql.connect(host="localhost", user="root", password="123456",
                           charset='utf8mb4',port=1306)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS siot")
    cur.close()
    conn.close()

def MakeTable():
    # 用户存储表，存储用户的用户名和用户编号，以及密码
    # 在本版本中密码暂时使用明文存储
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    user_sql = """CREATE TABLE IF NOT EXISTS user_login (
         username  CHAR(20) NOT NULL,
         password  CHAR(20),
         user_id INT primary key auto_increment)"""
    # 管理员存储表，存储管理员的用户名，用户编号，管理员编号
    admin_sql = """CREATE TABLE IF NOT EXISTS admin_login (
        username CHAR(20) NOT NULL,
        user_id  INT,
        admin_id INT primary key auto_increment)"""
    # 设备信息表，存储设备的编号，描述，设备主人id
    device_sql = """CREATE TABLE IF NOT EXISTS device_login (
        des CHAR(40) ,
        owner_id INT )"""
    # 验证码验证表，暂时还未使用redis，在后续更新中使用redis进行验证码验证。
    verify_sql="""CREATE TABLE IF NOT EXISTS verify_login (
        email CHAR(40),
        verify_code INT )"""
    curs = conn.cursor()
    curs.execute(user_sql)
    curs.execute(admin_sql)
    curs.execute(device_sql)
    curs.execute(verify_sql)
    conn.close()
    curs.close()
    print("init successfully")
    # return (conn,curs)

# # 测试代码
# if __name__ == '__main__':
#     MakeDatabase()
#     MakeTable()