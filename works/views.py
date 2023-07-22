from rest_framework import generics
from .models import Works,Category,Tag
from .serializers import WorksSerializer,SimpleWorksSerializer,CategorySerializer,TagSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class WorksListCreateView(generics.ListCreateAPIView):
    queryset = Works.objects.order_by('-created_at')  # '-' indicates descending order
    serializer_class = SimpleWorksSerializer

    @method_decorator(cache_page(60*15))  # Cache the response for 15 minutes (optional)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class WorksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer