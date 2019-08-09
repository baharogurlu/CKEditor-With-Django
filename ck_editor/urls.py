from . import views
from django.urls import path

app_name = 'ck_editor'

urlpatterns =[
    path('', views.index, name='index'),
    path('posts', views.post_list,name='post_list'),
    path('posts/create', views.post_create, name='post_create'),
    path('posts/<pk>/update', views.post_update, name='post_update'),
    path('posts/<pk>/delete', views.post_delete, name='post_delete'),
]