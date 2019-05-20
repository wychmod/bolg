from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment
# 实例化ORM模型
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
login_manager = LoginManager()
moment = Moment()
def ext_init(app):
    db.init_app(app)
    Bootstrap(app)
    migrate.init_app(app=app)
    mail.init_app(app)
    moment.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'user.login' # 处理登录的端点 也就是说如果你访问了需要登录才能访问的路由 那么就调到 user.login 的视图函数去
    login_manager.login_message = '请登录后在访问'
    login_manager.session_protection = 'strong' # 最强保护级别 出现任何问题 都会自动退出
