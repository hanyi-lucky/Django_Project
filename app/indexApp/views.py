from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 编写视图函数
def hello(request):
    return HttpResponse("<h1>你好 Django</h1>")


# 视图函数接受参数
# 其中 name 和 age 就是从 url 中提取出来的
# 请求的 url: /test_one_api/Bear/18
# 第一个参数 request 是 Django 自动传递的对象，包含请求所有信息，name和age 是从 URL 提取出来的动态参数
# 该视图函数的作用是处理 URL 请求，并返回包含动态数据的响应
def test_one_api(request, name, age):
    return HttpResponse(f"<h1>姓名：{name}</h1><h1>年纪：{age}</h1>")


def test_two_api(request, x, y):
    return HttpResponse(f"<h1>x轴：{x}<h1><h1>y轴：{y}<h1>")


def page_2026(request):
    print("获取 URL 字符串: ", request.path_info)
    print("获取 Get 请求方式的所有数据: ", request.GET)
    print("获取 POST 请求方式的所有数据:", request.POST)
    print("获取包含所有的上次文件信息: ", request.FILES)
    print("获取 cookie 所有键值字符串: ", request.COOKIES)
    print("获取当前会话信息: ", request.session)
    print("获取请求体的内容: ", request.body)
    print("获取请求协议: ", request.scheme)
    print("请求的完整路径: ", request.get_full_path())
    print("请求中的元数据（消息头）: ", request.META)
    print("获取客户端的 ip 地址: ", request.META['REMOTE_ADDR'])

    html = "<h1>这是第一个页面<h1>"
    return HttpResponse(html)


# app应用/views.py

import datetime
import json
import os

from django.conf import settings


# 返回纯文本，展示“动态内容”
def current_time(request):
    # 获取格式化时间字符串
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 构造要返回的文本内容
    txt = f"服务器当前时间：{now}"
    return HttpResponse(
        txt,  # 响应正文
        content_type='text/plain; charset=utf-8'  # 告诉浏览器这是纯文本，UTF-8 编码
    )


# 返回 Json，展示“json api”
def api_info(request):
    # 准备要返回的字典
    data = {
        'name': 'Bear',
        'age': '18',
        'path': request.path_info
    }
    # 转为 JSON 字符串，不转义中文
    json_str = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
        json_str,  # 响应正文（JSON 字符串）
        content_type='application/json',  # 声明 JSON 类型
        status=200  # 明确返回 200 OK
    )


# 流式下载文件页面
def file_page(request):
    return render(request, 'file.html')


# 流式下载文件
def file(request, file_name):
    # 根据文件名拼接出磁盘绝对路径
    # 注意：MEDIA_ROOT 里已经包含 media 目录了，直接拼文件名就行
    # 之前这里又写了一层 'media'，拼成了 media/media/txt.txt，路径多了一层导致文件找不到
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # 如果文件不存在，直接返回 404
    if not os.path.exists(file_path):
        return HttpResponse('文件不存在', status=404)

    # 内部生成器：逐块读取文件，避免一次性加载到内存
    def file_iterator(path, chunk_size=8192):
        # 以二进制只读模式打开文件
        with open(path, 'rb') as f:
            # 无限循环，直到文件读完
            while True:
                # 每次读取 8 KB
                chunk = f.read(chunk_size)
                # 没有数据表示读到 EOF
                if not chunk:
                    break
                # 生成器逐块产出数据
                yield chunk

    # 构造流式下载响应
    response = HttpResponse(
        file_iterator(file_path),  # 给 HttpResponse 一个可迭代对象即可流式输出
        content_type='application/octet-stream'  # 通用二进制流
    )
    # 设置 Content-Disposition 让浏览器弹出“另存为”对话框
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
