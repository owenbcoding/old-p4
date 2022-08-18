from . import views
from django.urls import path
 
# importing views from views..py
#from .views import index
 
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]

