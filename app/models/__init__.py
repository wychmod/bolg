from .user import User
from .posts import Posts
from app.extensions import db

# 创建存储多对多的中间表 collections
collections = db.Table('collections',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('posts_id',db.Integer,db.ForeignKey('posts.id')),
)
