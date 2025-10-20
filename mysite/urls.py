"""mysite URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# 定义一个简单的视图函数，显示个人信息
def hello_world(request):
    return HttpResponse("<h1>何佳佳</h1><p>学号：20231201032</p><p>Welcome to my Django application.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),  # 根URL直接返回Hello World
    path('hello/', hello_world),  # /hello/路径也返回Hello World
]