#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
     path('shop/',views.ShopListCreateView.as_view(),name='role'),

]