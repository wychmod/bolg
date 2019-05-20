## 博客

## 一、目录层级

```python
blog/
	app/
    	templates/ 模板目录
        	common/
        static/
        	img/
            css/
            js/	
            upload/	文件上传图片目录
        forms/	表单文件
        	__init__.py
        views/	视图文件
        	__init__.py
        models/	模型文件
        	__init__.py
        __init__.py
        config.py 	配置文件
        extensions.py	加载第三方扩展库文件
        email.py	发送邮件文件
        	
    migrations/
    venv/
    manage.py
```



## 二、虚拟环境

虚拟环境就是一个全新的环境  除了自带的包  在新的环境中 安装当前所需要的扩展库

#### (1)**安装虚拟环境**

pip install virtualenv

#### (2) 创建虚拟环境

virtualenv venv(虚拟环境名称)

#### (3) 启动

venv\Scripts\activate

#### (4) 退出虚拟环境

venv\Scripts\deactivate.bat



## 三、处理用户状态维持的操作

flask-login模块

pip install flask-login





## 四、分页

```python
paginate
实例化参数
	page	当前的页码
    per_page	每页显示数据的条数
    error_out	当分页查询出错 是否抛出错误 默认True
    
pagination	分页对象
属性:
    	items 当前页面所有数据
        page	当前页码
        pages	所有页码
        prev_num	上一页的页码
        next_num	下一页的页码
        has_prev	是否有上一页
        has_next	是否有下一页
        
方法:
    prev	上一页的分页对象
    next	下一页的分页对象
    iter_pages	是一个迭代器 返回所有页码
```



## 五、待完成

1. 博客管理
   + 分页
   + 搜索（和导航中的搜索一样的 多的条件过滤是 必须搜索的是自己发表的）
   + 删除 需要改变成 点击删除时 问是否删除也就是js中的cofirm方法 如果点击确定删除则删除  否则取消删除
2. 个人中心
   + 信息查看
   + 更改用户名
   + 更改密码
   + 更改邮箱
   + 头像上传缩放
3. 周三（领着写的）
   + 博客收藏 取消收藏
   + 博客收藏管理
   + 博客的评论与回复
   + flask-restful