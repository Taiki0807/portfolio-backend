from django.shortcuts import render
from rest_framework import generics,status
from .models import Post, Category,Tag
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer,TagSerializer
from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.http import JsonResponse
from google.cloud import storage
import random,string
import os
from datetime import datetime
from django.utils import timezone
from google.oauth2 import service_account

#google cloud storageのクライアントインスタンスを作成
key_path = './portfolio-377405-3a43641d221e.json'
credential = service_account.Credentials.from_service_account_file(key_path)

project_id = "portfolio-377405"
client = storage.Client(project_id, credentials=credential)

#バケットのインスタンスを取得
bucket = client.bucket('portfolio-hosokawalab')

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

def upload(file):
    dt_now = datetime.now()
    dt_now_str = dt_now.strftime('%Y%m%d%H%M%S%f')
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
    file_name_with_extention = dt_now_str + "_" + ''.join(randlst) + '.jpg'
    fs = FileSystemStorage()
    filename = fs.save("images/" + file_name_with_extention, file)
    blob = bucket.blob(file_name_with_extention)
    blob.upload_from_filename(fs.path(filename))
    os.remove(fs.path(filename))

    return blob.public_url


class ImageRegisterAPIView(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.data["editormd-image-file"]
        object_url = upload(file)
        return JsonResponse({'success': 1,'message': "成功",'url': object_url})