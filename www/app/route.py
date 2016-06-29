#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-05 22:51:06
# @Author  : moling (365024424@qq.com)
# @Link    : #
# @Version : 0.1

from app.frame import get
from app.frame.halper import Page, set_valid_value, markdown_highlight
from app.models import Blog


# 测试
@get('/test')
async def test():
    return {
        '__template__': 'uk-base.html'
    }


# 首页
@get('/')
async def index():
    return 'redirect:/bootstrap/'


@get('/{template}/')
async def home(template, *, page='1', size='10'):
    num = await Blog.countRows()
    page = Page(num, set_valid_value(page), set_valid_value(size, 10))
    if num == 0:
        blogs = []
    else:
        blogs = await Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
    for blog in blogs:
        blog.content = markdown_highlight(blog.content)
    return {
        '__template__': '%s-blogs.html' % (template),
        'blogs': blogs,
        'page': page
    }


# 注册页面
@get('/register')
def register():
    return {
        '__template__': 'bootstrap-register.html'
    }


# 登陆页面
@get('/signin')
def signin():
    return {
        '__template__': 'bootstrap-signin.html'
    }


# 博客页面
@get('/blog/{id}')
async def get_bolg(id):
    blog = await Blog.find(id)
    blog.content = markdown_highlight(blog.content)
    return {
        '__template__': 'bootstrap-blog.html',
        'blog': blog
    }


# 管理页面
@get('/manage')
def manage():
    return 'redirect:/manage/blogs'


# 管理用户、博客、评论
@get('/manage/{table}')
def manage_table(table):
    return {
        '__template__': 'bootstrap-manage.html',
        'table': table,
    }


# 创建博客
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'bootstrap-blog_edit.html'
    }


# 修改博客
@get('/manage/blogs/edit')
def manage_edit_blog():
    return {
        '__template__': 'bootstrap-blog_edit.html'
    }