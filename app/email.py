from flask_mail import Message
from flask import current_app,render_template
from app.extensions import mail
from threading import Thread

def async_send_mail(app,msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject,to,temName,**kwargs):
    '''
    发送邮件
    :param subject: 主题
    :param to: 发送给谁
    :param temName: 模板名称
    :return:
    '''
    # 获取我们真正实例化的flask对象 app
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=current_app.config['MAIL_USERNAME'])
    msg.html = render_template('email/'+temName+'.html',**kwargs)
    thr = Thread(target=async_send_mail,args=(app,msg))
    thr.start()# 开启线程