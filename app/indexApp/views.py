from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#编写视图函数
def hello(request):
    return HttpResponse("<h1>你好 Django</h1>")

# 视图函数接受参数
# 其中 name 和 age 就是从 url 中提取出来的
# 请求的 url: /test_one_api/Bear/18
# 第一个参数 request 是 Django 自动传递的对象，包含请求所有信息，name和age 是从 URL 提取出来的动态参数
# 该视图函数的作用是处理 URL 请求，并返回包含动态数据的响应
def test_one_api(request,name,age):
    return HttpResponse(f"<h1>姓名：{name}</h1><h1>年纪：{age}</h1>")

def test_two_api(request,x,y):
    return HttpResponse(f"<h1>x轴：{x}<h1><h1>y轴：{y}<h1>")

