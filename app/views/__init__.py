from .main import main # 导入首页的蓝本对象
from .user import user # 导入用户处理的蓝本对象
from .posts import posts # 导入博客处理的蓝本对象
from .owncenter import own # 导入个人中心蓝本对象
# 蓝本对象的列表
default_blueprint = [
    (main,''),
    (user,''),
    (posts,''),
    (own,''),
]

# 进行蓝本文件的注册
def register_blueprint(app):
    for blueprint,prefix in default_blueprint:
        app.register_blueprint(blueprint,url_prefix=prefix)