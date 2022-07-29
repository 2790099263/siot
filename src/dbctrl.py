import random
import api
# 如果之前有验证码，就直接覆盖，没有就插入
# 仅在本版本使用，后续使用redis进行验证码验证
def InsertVerifyCode(email):
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    return_code = 0
    ifexists_sql = '''SELECT verify_code from verify_login where email="'''+str(email)+'"'
    # print(ifexists_sql)
    res = curs.execute(ifexists_sql)
    if res > 0 :
        p=curs.fetchall()
        # print(p[0][0])
        new_code=random.randint (100000 , 999999)
        return_code = new_code
        # print("newcode"+str(new_code))
        updatecode_sql='''update verify_login set verify_code=''' \
                       +str(new_code)+''' where email="''' \
                       +str(email)+'"'
        # print(updatecode_sql)
        curs.execute(updatecode_sql)

    else:
        verify_code = random.randint (100000 , 999999)
        return_code = verify_code
        # print("verify_code"+str(verify_code))
        insertcode_sql='''insert into verify_login (email, verify_code) values ("''' \
                       + str(email)+'",' \
                       +str(verify_code)+")"
        # print(insertcode_sql)
        curs.execute(insertcode_sql)

    conn.commit()
    conn.close()
    curs.close()
    return return_code
# 在数据库中验证验证码
def VerifyCode(email,type_code):
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    search_sql = '''SELECT verify_code from verify_login where email="'''+str(email)+'"'
    res = curs.execute(search_sql)
    if res == 0:
        return 0
    re  = curs.fetchall()
    # print(re)
    if str(re[0][0]) == type_code :
        del_sql = "delete from verify_login where email="   \
            +'"' + str(email) + '"'
        curs.execute(del_sql)
        conn.commit()
        return 1
    else:
        return 0
    conn.close()
    curs.close()
# 插入用户，返回user_id,如果返回的是0，则查无此人
def InsertUser(username,passwd):
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    serch_sql="insert into user_login (username, password) VALUES ("    \
            + '"' + str(username) + '"'+','+'"'+str(passwd)+'"'+')'
    curs.execute(serch_sql)
    conn.commit()
    res_sql = '''select user_id from user_login where username="''' \
        +str(username) +'"'
    res = curs.execute(res_sql)
    if res == 0:
        curs.close()
        conn.close()
        return 0
    re = curs.fetchall()
    curs.close()
    conn.close()
    return re[0][0]
# 验证用户的用户名和密码是否相同，返回是否
def VerifyUser(username,type_passwd):
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    verify_sql = 'select password from user_login where  username="'    \
        +str(username)+'"'
    res=curs.execute(verify_sql)
    if res==0:
        curs.close()
        conn.close()
        return 0
    re=curs.fetchall()
    if re[0][0]==str(type_passwd):
        curs.close()
        conn.close()
        return 1
    curs.close()
    conn.close()
    return 0
# 获取用户id，返回用户id
def GetUserId(username):
    db = api.GetDatabase()
    conn = db[0]
    curs = db[1]
    get_sql = 'select user_id from  user_login where username="'    \
        + str(username) + '"'
    res = curs.execute(get_sql)
    if res==0:
        curs.close()
        conn.close()
        return 0
    re = curs.fetchall()
    curs.close()
    conn.close()
    return re[0][0]


# if __name__ == '__main__':
    # InsertVerifyCode("2790099263@qq.com")
    # InsertVerifyCode("2456727063@qq.com")
    # print (VerifyCode("2790099263@qq.com",501564))
    # print (VerifyUser("ls2719","1234"))
    # print(GetUserId("lsc2719"))