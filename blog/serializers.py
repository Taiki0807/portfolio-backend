from rest_framework import serializers
from .models import Category, Tag, Post
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.fenced_code import FencedCodeExtension
import re


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'color',)

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('main_text', 'created_at','updated_at')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(many=True)
    main_text = serializers.SerializerMethodField()
    toc_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_main_text(self, instance):
        main_text = instance.main_text.replace("[TOC]", "")  # [TOC] を削除
        return markdown.markdown(main_text, extensions=["extra",'tables'])
    
    def get_toc_text(self, instance):
        main_text = re.sub(r'```.*?```', '', instance.main_text, flags=re.DOTALL)
        toc_html = markdown.markdown(main_text, extensions=[TocExtension(toc_depth=1)])
        toc_start_index = toc_html.find('<ul>')
        toc_end_index = toc_html.rfind('</ul>') + len('</ul>')
        return toc_html[toc_start_index:toc_end_index]