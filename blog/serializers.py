from rest_framework import serializers
from .models import Category, Post
import markdown
from markdown.extensions.toc import TocExtension


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'color',)


class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('main_text', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    main_text = serializers.SerializerMethodField()
    toc_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_main_text(self, instance):
        main_text = instance.main_text.replace("[TOC]", "")  # [TOC] を削除
        return markdown.markdown(main_text)
    
    def get_toc_text(self, instance):
        toc_html = markdown.markdown(instance.main_text, extensions=[TocExtension(toc_depth=1)])
        toc_start_index = toc_html.find('<ul>')
        toc_end_index = toc_html.rfind('</ul>') + len('</ul>')
        return toc_html[toc_start_index:toc_end_index]