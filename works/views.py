from rest_framework import generics
from .models import Works,Category,Tag
from .serializers import WorksSerializer,SimpleWorksSerializer,CategorySerializer,TagSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class WorksListCreateView(generics.ListCreateAPIView):
    queryset = Works.objects.all()
    serializer_class = SimpleWorksSerializer

class WorksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer