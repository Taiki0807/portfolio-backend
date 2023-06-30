from django.contrib import admin
from .models import Works, Category, Tag

admin.site.register(Category)
admin.site.register(Works)
admin.site.register(Tag)