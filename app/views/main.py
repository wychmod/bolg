from flask import Blueprint,render_template,request,current_app
from app.models import Posts # 导入博客模型类
# 首页的蓝本文件
main = Blueprint('main',__name__)
# 127.0.0.1:5000/index/1/
@main.route('/')
@main.route('/index/')
def index():
    try:
        page = int(request.args.get('page',1))
    except:
        page = 1
    # 查出所有人可见的博客并按照时间降序 展示
    pagination = Posts.query.filter(Posts.pid==0,Posts.state==True).order_by(Posts.timestamp.desc()).paginate(page,current_app.config['PAGE_NUM'],False)
    # 获取当前页面所有数据
    data = pagination.items
    return render_template('main/index.html',p=data,pagination=pagination)


