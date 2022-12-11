from . import views
from django.urls import path
 
 
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/<int:blog_post_id>/', views.PostDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('blog/create', views.create_post, name='create_post'),
    path('blog/delete/<int:blog_post_id>', views.delete_post, name='delete_post'),
    path('contact/', views.contact, name="contact"),
]

