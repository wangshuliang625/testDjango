#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/11/12 14:53
# @Author : WangShu
# @FileName: urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    url(r'^(\d+)$', views.detail),
]