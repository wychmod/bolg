from flask import Blueprint,redirect,render_template,flash,url_for,request,current_app,jsonify
from app.models import Posts # 导入博客模型
from app.forms import SendPosts # 导入发表博客的form表单
from flask_login import current_user
from sqlalchemy import or_ # 导入或操作

posts = Blueprint('posts',__name__)

# 必须登陆后才能发表
@posts.route('/send_posts/',methods=['GET','POST'])
def send_posts():
    form = SendPosts()
    if not current_user.is_authenticated:
        flash('请先登陆后在放表')
    elif form.validate_on_submit():
        p = Posts(title=form.title.data,article=form.article.data,user=current_user)
        p.save()
        flash('发表成功！')
        return redirect(url_for('posts.send_posts'))
    return render_template('posts/send_posts.html',form=form)


# 博客显示详情的视图函数
@posts.route('/posts_detail/<int:pid>/')
def posts_detail(pid):
    # 评论和回复展示的表单类
    form = SendPosts()
    p = Posts.query.get(pid)
    # 查询出所有当前博客的评论和回复的内容
    comment = Posts.query.filter(Posts.path.contains(str(pid))).order_by(Posts.path.concat(Posts.id))
    return render_template('posts/posts_detail.html',p=p,form=form,comment=comment)


# 博客评论和回复功能的视图函数
@posts.route('/comment/',methods=['GET','POST'])
def comment():
    id = request.form.get('id')
    if current_user.is_authenticated:
        try:
            # 判断是评论还是回复  评论的话pid为博客的id  回复的话 pid为评论人的id
            rid = request.form.get('rid')
            if rid:
                pid = rid
            else:
                pid = id
            article = request.form.get('article')
            path = request.form.get('path')
            print(path)
            Posts(article=article,pid=pid,path=path+str(pid)+',',user=current_user).save()
            flash('评论成功')
        except:
            flash('评论失败')
    else:
        flash('您还没有登录 请先登录在进行操作')
    # 重定向回到博客详情
    return redirect(url_for('posts.posts_detail',pid=id))




# 博客搜索
@posts.route('/search/',methods=['GET','POST'])
def search():
    con = request.form.get('search','')
    if not con:
        con = request.args.get('search','')
    try:
        page = int(request.args.get('page',1))
    except:
        page = 1

    # 我希望的搜索 标题和内容包含都搜索到 并且在展示的时候 换成红色的搜索内容的字
    pagination = Posts.query.filter(or_(Posts.title.contains(con),Posts.article.contains(con)),Posts.pid==0,Posts.state==True).order_by(Posts.timestamp.desc()).paginate(page,current_app.config['PAGE_NUM'],False)
    data = pagination.items
    return render_template('posts/search_detail.html',data=data,con=con,pagination=pagination)


# 博客收藏与取消收藏
@posts.route('/dofavorite/')
def dofavorite():
    try:
        # 将博客id转换成int类型
        id = int(request.args.get('id'))
        # 判断当前是否收藏
        if current_user.is_favorite(id):
            # 收藏执行取消收藏
            current_user.del_favorite(id)
        else:
            # 执行添加收藏
            current_user.add_favorite(id)
        return jsonify({'code': 200})
    except:
        return jsonify({'code': 500})
