from flask import Flask
# 导入当前网站的配置类
from app.config import config
# 加载所有的第三方扩展库
from app.extensions import ext_init
# 导入注册的蓝本函数
from app.views import register_blueprint
from app.models import Posts

def create_app(configName):
    app = Flask(__name__)
    # 加载网站配置
    app.config.from_object(config[configName])
    # 加载所有第三方扩展库
    ext_init(app)
    # 注册蓝本
    register_blueprint(app)
    # 初始化加载自定义过滤器
    add_filter(app)
    return app

# 定义一个加载自定义过滤器的函数
def add_filter(app):
    # 博客内容显示超出几个长度 显示...
    @app.template_filter()
    def showEllipsis(str,length=5):
        if len(str)>length:
            str = str[0:5]+'...'
        return str
    # 搜索出来的内容 替换成红色
    @app.template_filter()
    def replace_red(str,con):
        if str:
            str = str.replace(con,'<span style="color:red;">'+con+'</span>')
        return str
    # 获取回复人的名字的过滤器
    @app.template_filter()
    def replayName(rid):
        return Posts.query.get(int(rid)).user.username