# Generated by Django 4.1.7 on 2023-03-08 06:15

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_text',
            field=mdeditor.fields.MDTextField(verbose_name='本文'),
        ),
    ]
