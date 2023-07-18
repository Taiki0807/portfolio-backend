from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('upload/', views.ImageRegisterAPIView.as_view(), name="imageRegister"),
]