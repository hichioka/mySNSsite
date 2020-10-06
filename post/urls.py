from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_edit/', views.post_edit, name='post_edit'),
    path('post_remove/', views.post_remove, name='post_remove'),
]