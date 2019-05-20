from flask import Blueprint,render_template,flash,redirect,url_for
from flask_login import login_required,current_user
from app.models import Posts #导入发表博客模型
from app.forms import SendPosts # 导入发表博客表单类
from datetime import datetime

own = Blueprint('owncenter',__name__)

# 博客管理
@own.route('/posts_manager/')
@login_required
def posts_manager():
    data = current_user.posts.filter(Posts.pid==0).order_by(Posts.timestamp.desc())
    return render_template('owncenter/posts_manager.html',data=data)


# 博客管理 删除
@own.route('/posts_delete/<int:id>/')
@login_required
def posts_delete(id):
    Posts.query.get(id).delete()
    flash('博客删除成功！')
    return redirect(url_for('owncenter.posts_manager'))

# 博客编辑
@own.route('/edit_posts/<int:id>/',methods=['GET','POST'])
@login_required
def edit_posts(id):
    form = SendPosts()
    p = Posts.query.get(id) # 通过博客id查询出博客对象
    if form.validate_on_submit():
        p.title = form.title.data
        p.article = form.article.data
        p.timestamp = datetime.utcnow()
        p.save()
        flash('博客修改成功！')
        # 重定向到博客管理
        return redirect(url_for('owncenter.posts_manager'))
    # 添加默认值
    form.title.data = p.title
    form.article.data = p.article
    return render_template('owncenter/edit_posts.html',form=form)


# 博客收藏管理
@own.route('/favorite_manager/')
def favorite_manager():
    # 查询出当前用户的所有收藏
    favorites = current_user.favorites.all()
    return render_template('owncenter/favorites_manager.html',data=favorites)

# 执行取消收藏的功能
@own.route('/del_favorite/<int:id>/')
def del_favorite(id):
    try:
        # 判断当前是否收藏
        if current_user.is_favorite(id):
            # 收藏执行取消收藏
            current_user.del_favorite(id)
    except:
        pass
    # 取消收藏后 回到收藏管理
    return redirect(url_for('owncenter.favorite_manager'))