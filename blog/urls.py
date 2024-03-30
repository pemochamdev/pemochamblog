from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog-list'),
    path('blog-detail/<slug>/', views.blog_detail, name='blog-detail'),
]
