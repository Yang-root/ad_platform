"""广告平台接口路由。"""
from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello, name="hello"),
]
