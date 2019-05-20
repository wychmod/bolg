from app.extensions import db
from .db_base import DB # 导入模型操作的基类
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask import current_app
from flask_login import UserMixin
from app.extensions import login_manager
from .posts import Posts

# 创建user表
class User(UserMixin,DB,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(12),index=True)
    password_hash = db.Column(db.String(120))
    age = db.Column(db.Integer,default=18)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(50),index=True)
    icon = db.Column(db.String(70),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False) # 账户是否激活 默认没激活
    """
    posts 是当前user模型的关联属性 可以通过当前用户对象获取 发表了哪些博客
    参数
    Posts 建立关联的模型
    backref 给关联的模型添加的字段属性 user
    lazy 加载时机  返回查询集 可以再次进行二次过滤 User.query+过滤器 如果不给lazy属性 则返回结果的列表 而不是查询集
    """
    posts = db.relationship('Posts',backref='user',lazy='dynamic')
    # secondary 是多对多时 指定查询数据的中间表
    # backref给另一方的多 设置查询结果为查询集  可以进行查询结果的过滤
    favorites = db.relationship('Posts',secondary='collections',backref=db.backref('users',lazy='dynamic'),lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('该属性不可读')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    # 验证密码正确性
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


    # 生成token的方法
    def generate_token(self):
        # 默认1小时token有效 过了1小时 解析失败 报错
        s = Seralize(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self.id})


    # 验证token 并进行账户的激活
    @staticmethod
    def check_token(token):
        s = Seralize(current_app.config['SECRET_KEY'])
        # 在解析和激活操作的过程中 出现任何异常 都是激活失败
        try:
            id = s.loads(token)['id']
            u = User.query.get(int(id))
            if not u.confirm:
                u.confirm = True
                u.save()
            return True
        except:
            return False

    # 判断是否收藏的方法
    def is_favorite(self,id):
        # 查询当前所有的收藏
        favorites = self.favorites.all()
        for f in favorites:
            if f.id == id:
                return True
        return False

    #  执行收藏的方法
    def add_favorite(self,id):
        self.favorites.append(Posts.query.get(id))
        db.session.commit()

    # 取消收藏的方法
    def del_favorite(self,id):
        self.favorites.remove(Posts.query.get(id))
        db.session.commit()

# 回调函数 实时获取user表中的数据
@login_manager.user_loader
def user_loader(userid):
    return User.query.get(int(userid))