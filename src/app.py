from flask import Flask,request
import api
import init
app = Flask(__name__)
# 用户注册模块，通过post传递参数，username如果被使用return ERROR
# 返回用户id
@app.route('/register',methods=['POST'])
def UserRegister():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email    = request.form.get('email')
        code     = request.form.get('code')
        if api.GetVerifyUser(username) == 1:
            return "your username has been used"
        print(username,password,email,code)
        print(type(username),type(password),type(email),type(code))
    else:
        return "please post your sends"
    return str(api.UserRegister(username,password,email,code))
    # return "get successfully"
# 用户登录模块
@app.route('/login',methods=['POST'])
def UserLogin():
    username = request.form['username']
    password = request.form['password']
    res = api.UserInter(username,password)
    if res == 0:
        return "enter failed"
    else:
        return "enter successfully"
# 获取验证码模块
@app.route('/getverifycode',methods=['POST'])
def GetVerifyCode():
    username = request.form['username']
    email    = request.form['email']
    res = api.GetVerifyCode(username,email)
    # print(res)
    return "send successfully"

if __name__ == '__main__':
    init.MakeDatabase()
    init.MakeTable()
    app.run("0.0.0.0",debug=True)