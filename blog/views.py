from django.shortcuts import render
from rest_framework import generics
from .models import Post, Category,Tag
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer,TagSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer