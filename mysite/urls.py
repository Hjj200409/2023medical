"""mysite URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# 定义一个简单的视图函数，返回Hello World响应
def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1><p>Welcome to my Django application.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),  # 根URL直接返回Hello World
    path('hello/', hello_world),  # /hello/路径也返回Hello World
]