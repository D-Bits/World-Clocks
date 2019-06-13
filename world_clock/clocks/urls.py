from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('africa/', views.africa_times, name='africa')
]