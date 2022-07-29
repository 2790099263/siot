# api.py author:lsc time:2022/07/15
import pymysql
import dbctrl
import send
# 连接数据库，将在后续版本变为从配置文件中读取信息
def GetDatabase():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='siot',
        port=1306,
        charset='utf8mb4'
    )
    curs = conn.cursor()
    return (conn,curs)

# 用户注册模块，0为注册失败，other为userid;
def UserRegister(username,password,email,code):
    if dbctrl.VerifyCode(email,code) == 0:
        return 0
    return dbctrl.InsertUser(username,password)
# 用户登录模块，0表示登录失败，1表示登录成功
def UserInter(username,password):
    return dbctrl.VerifyUser(username,password)
# 获取验证码模块,返回验证码
def GetVerifyCode(user,email):
    # code=random.randint(100000,999999)
    code = dbctrl.InsertVerifyCode(email)
    send.SendEmail(user,email,code)
    return code
# 该用户名已经被注册的话就返回1，否则返回0
def GetVerifyUser(username):
    if dbctrl.GetUserId(username) == 0:
        return 0
    else:
        return 1
# if __name__ == "__main__":
#     db = GetDatabase()
#     print(db)
#     print(type(db))
#     conn = db[0]
#     curs = db[1]
#     print(conn)
#     print(curs)