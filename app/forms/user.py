from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,PasswordField
from wtforms.validators import ValidationError,DataRequired,Length,Email,EqualTo
# 导入user模型类
from app.models import User
# 表单注册类
class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空！'),Length(min=6,max=12,message='用户名在6~12位之间')],render_kw={'placeholder':'请输入用户名'})
    userpass = PasswordField('密码',validators=[DataRequired(message='密码不能为空！'),Length(min=6,max=12,message='密码在6~12位之间')],render_kw={'placeholder':'请输入密码'})
    confirm = PasswordField('确认密码',validators=[EqualTo('userpass',message='密码与确认密码不一致')],render_kw={'placeholder':'请输入确认密码'})
    email = StringField('邮箱',validators=[DataRequired(message='邮箱不能为空'),Email(message='请输入正确的邮箱地址')],render_kw={'placeholder':'请输入用于激活账户的邮箱地址'})
    submit = SubmitField('注册')
    # 判断用户名是否唯一性
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户已存在')

    # 判断邮箱是否具有唯一性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在')

# 登录的表单
class Login(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空！'),Length(min=6,max=12,message='用户名在6~12位之间')],render_kw={'placeholder':'请输入用户名'})
    userpass = PasswordField('密码',validators=[DataRequired(message='密码不能为空！'),Length(min=6,max=12,message='密码在6~12位之间')],render_kw={'placeholder':'请输入密码'})
    submit = SubmitField('登录')
    # 判断用户名是否存在
    def validate_username(self,field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户不存在')