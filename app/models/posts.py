from app.extensions import db
from .db_base import DB
from datetime import datetime

# 博客模型
class Posts(DB,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(15),index=True)
    article = db.Column(db.Text)
    pid = db.Column(db.Integer,default=0)
    path = db.Column(db.String(255),default='0,')
    visit = db.Column(db.Integer,default=0)# 访问量
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    state = db.Column(db.Boolean,default=True) # 是否所有人可见
    uid = db.Column(db.Integer,db.ForeignKey('user.id')) # 添加外键 可以通过博客获取发表的用户  也可以通过用户 查看发表了哪些博客