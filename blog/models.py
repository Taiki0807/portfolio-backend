from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
import markdown

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=100)
    color = models.CharField('色(16進数)', max_length=7, default='#000000')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=40)
    thumbnail = models.ImageField('サムネイル', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    lead_text = models.TextField('紹介文')
    main_text = MDTextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', auto_now=True)


    class Meta:
        ordering = ['-updated_at']

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
