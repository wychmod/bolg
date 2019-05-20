import os
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    # 秘钥
    SECRET_KEY = '21s34desxas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #  发送邮件的配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # 每页显示数据的条数
    PAGE_NUM = 2


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'dev_blog.sqlite')


# 测试环境的配置
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'test_blog.sqlite')



# 生产环境的配置
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'blog.sqlite')

# 类的别名
config = {
    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig
}