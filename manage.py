from flask_script import Manager
from app import create_app
from flask_migrate import MigrateCommand

# 创建app的方法
app = create_app('default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()