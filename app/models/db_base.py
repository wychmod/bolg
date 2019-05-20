from app.extensions import db
# 封装一个增删改的类 简化我们当前的操作
class DB:
    # 添加一条数据的方法
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    # 添加多条的方法
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    # 定义删除的方法
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()