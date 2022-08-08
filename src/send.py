# time:2022/07/15 author:lsc
# send.py 验证码邮件发送模块，主要是给特定的邮箱发送验证码邮件，用来进行登录或者注册验证。
# 邮件发送与登录验证
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

def sendMail(message,Subject,sender_show,recipient_show,to_addrs,cc_show=''):
    # '''
    # :param message: str 邮件内容
    # :param Subject: str 邮件主题描述
    # :param sender_show: str 发件人显示，不起实际作用如："xxx"
    # :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
    # :param to_addrs: str 实际收件人
    # :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
    # '''
    # 填写真实的发邮件服务器用户名、密码
    user = 'XXXXXX@126.com'
    password = 'XXXXXXXXXXXXXXXXXX'
    # 邮件内容
    msg = MIMEText(message, 'plain', _charset="utf-8")
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["from"] = sender_show
    # 收件人显示，不起实际作用
    msg["to"] = recipient_show
    # 抄送人显示，不起实际作用
    msg["Cc"] = cc_show
    with SMTP_SSL(host="smtp.126.com",port=465) as smtp:
        # 登录发邮件服务器
        smtp.login(user = user, password = password)
        # 实际发送、接收邮件配置
        smtp.sendmail(from_addr = user, to_addrs=to_addrs.split(','), msg=msg.as_string())
def SendEmail(user,email,code):
    message = "尊敬的"+user+":\n   您好，您的验证码是：\n"+str(code)+"\n这边提醒您，验证码打死也不能告诉别人哦！"
    Subject = 'verify code'
    sender_show = 'siot platform'
    recipient_show = user
    to_addrs = email
    sendMail(message, Subject, sender_show, recipient_show, to_addrs)
# if __name__ =='__main__':
#     SendEmail("lsc2719","2790099263@qq.com",114514)
