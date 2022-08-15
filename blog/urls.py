from . import views
from django.urls import path
 
# importing views from views..py
#from .views import index
 
urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]

