from flask_wtf import FlaskForm
from wtforms.fields import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

# 发表博客类
class SendPosts(FlaskForm):
    title = StringField('标题',validators=[DataRequired(message='标题不能为空'),Length(min=6,max=12,message='标题长度在6~12位之间')])
    article = TextAreaField('博客内容',validators=[DataRequired('博客内容不能为空'),Length(min=6,max=500,message='博客内容在6~500字之间')])
