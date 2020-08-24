from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^contact/', views.contact, name='contact'),
    url('^vavilon/', views.vavilon, name='vavilon'),
    url('^baffetologic/', views.baffetologic, name='baffetologic'),
    url('^uorrenbaffet/', views.uorrenbaffet, name='uorrenbaffet'),
    url('^father/', views.father, name='father'),
    url('^think/', views.think, name='think'),
    url('^master/', views.master, name='master'),
    url('^money/', views.money, name='money'),
]
