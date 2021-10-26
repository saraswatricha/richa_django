from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
#   path('home/',home,name='blog_project'),
    path('',PostListView.as_view(),name='blog_project'),
    path('user/<str:username>',UserPostListView.as_view(),name='blog_user'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='blog_details'),
    path('detail/<int:pk>/update/',PostUpdateView.as_view(),name='blog_update'),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),
    path('post/new/',PostCreateView.as_view(),name='blog-create'),
    path('about/',about,name='about_home'),
    path('content/',content,name='content_home'),

    ]
