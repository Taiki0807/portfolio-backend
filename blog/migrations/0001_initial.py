# Generated by Django 4.1.7 on 2023-03-07 21:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='カテゴリ名')),
                ('color', models.CharField(default='#000000', max_length=7, verbose_name='色(16進数)')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル')),
                ('lead_text', models.TextField(verbose_name='紹介文')),
                ('main_text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='カテゴリ')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
