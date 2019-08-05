#0010
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #0019
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]