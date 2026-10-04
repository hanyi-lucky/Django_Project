"""
URL configuration for Django_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from indexApp import views
# 这里需要修改自己的 app 应用包
from indexApp.views import *

# Django 从配置文件中根据 ROOT_URLCONF 找到主路由文件；
# 默认情况下，该文件在项目同名目录下的 urls；
# 例如 mysite1/mysite1/urls.py
# Django 加载 主路由文件中的 urlpatterns 变量[包含很多路由的数组]
# 依次匹配 urlpatterns 中的 path，匹配到第一个合适的中断后续匹配
# 匹配成功-调用对应的视图函数处理请求，返回响应
# 匹配失败-返回 404 响应
urlpatterns = [
    # 如果找到对应的访问路径就直接返回
    # 如果访问的路由不在数组里边就会提示 404
    path('admin/', admin.site.urls),

    # path("访问地址", 执行的方法，name=为地址起别名) ⭐️
    # http://127.0.0.1:8000/page/2003

    #注册路由
    #这里函数就是自己写的 视图开发函数
    path('hello', views.hello),

    # <转换器类型: 变量名称> ⭐️
    # 不能有空格否则会报错
    path('test_one_api/<str:name>/<int:age>', test_one_api),

    # (?P<name>pattern)
    # (?P<变量名字>正则)
    # 不能有空格否则会报错
    # http://127.0.0.1:8000/12/Bear/33 必须后面接 1～2位数字/Bear/1～2位数字才可以访问
    # http://127.0.0.1:8000/ab/Bear/331 改为字母 ab/Bear/三位数字，则不能访问
    re_path(r"^(?P<x>\d{1,2})/Bear/(?P<y>\d{1,2})$", test_two_api),

    # 常用方法请求入口
    path(f"page_2026/", page_2026),



    # HttpResponse 返回纯文本，展示“动态内容”
    path("current_time/", current_time),

    # HttpResponse 返回 Json，展示“json api”
    path("api_info/", api_info),

    # HttpResponse 流式下载文件
    path("file_page/", file_page),
    path("file/<str:file_name>", file, name="file"),






]
