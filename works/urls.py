from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.WorksListCreateView.as_view(), name='works_list'),
    path('works/<int:pk>/', views.WorksRetrieveUpdateDestroyView.as_view(), name='works_detail'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
]