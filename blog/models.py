from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
import markdown

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=100)
    color = models.CharField('色(16進数)', max_length=7, default='#000000')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=40)
    thumbnail = models.ImageField('サムネイル', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    lead_text = models.TextField('紹介文')
    main_text = MDTextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',)  # 新しいデータから表示される
    
    def get_main_text(self, instance):
        return markdown.markdown(instance.main_text, extensions=['toc'])

    def __str__(self):
        return self.title
