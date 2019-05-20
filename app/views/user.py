from flask import Blueprint,render_template,flash,redirect,url_for
from app.forms import Register,Login # 导入表单注册类
from app.models import User # 导入user模型类
from app.email import send_mail
from flask_login import login_required,current_user,login_user,logout_user
user = Blueprint('user',__name__)

# 注册的视图函数
"""
注册功能步骤：
1. 判断用户名和 邮箱 是否唯一性
2. 将接收到的表单正确数据 进行存储(前提密码加密存储)
3. 生成token字符串(让用户点击账户激活的时候 我们服务端得知道是谁来激活的)
4. 配置发送邮件的代码
5. 发送邮件携带token
6. 用户点击进行账户激活
"""
@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        try:
            u = User(username=form.username.data,password=form.userpass.data,email=form.email.data)
            u.save()
            # 获取token字符串
            token = u.generate_token()
            # 发送邮件
            send_mail('邮件激活',u.email,'activate',username=u.username,token=token,endpoint='user.activate')
            flash('注册成功 请前往邮箱进行账户的激活')
            return redirect(url_for('user.login'))
        except:
            flash('用户注册失败')
    return render_template('user/register.html',form=form)

# 邮件激活处理的视图
@user.route('/activate/<token>/')
def activate(token):
    # 判断当前是否激活成功！
    if User.check_token(token):
        flash('激活成功 请登录')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败！请重新在次激活')
    return redirect(url_for('user.register'))


# 登录的视图函数
"""
接收到用户数据以后
验证密码是否正确
不正确则请输入正确的密码
正确的话维持当前用户的状态 保持登录状态
"""
@user.route('/login/',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter(User.username==form.username.data).first()
        if not u.check_password(form.userpass.data):
            flash('请输入正确的密码')
        elif not u.confirm:
            flash('您的账户还没有进行激活 请激活后在进行登录')
        else:
            flash('登录成功')
            login_user(u) # 维持登录状态的保持
            return redirect(url_for('main.index'))
    return render_template('user/login.html',form=form)

# 退出登录
@user.route('/logout/')
def logout():
    logout_user()
    flash('退出成功！')
    return redirect(url_for('main.index'))