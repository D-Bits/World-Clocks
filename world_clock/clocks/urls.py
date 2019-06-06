from django.urls import path
from . import views
from .views import AfricaList, index

urlpatterns =[
    path('', views.index, name='index'),
    path('africa/', AfricaList.as_view(), name='africa')
]