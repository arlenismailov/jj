# Generated by Django 5.0.6 on 2024-06-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption_en',
            field=models.CharField(max_length=100, null=True, verbose_name='описания'),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='описания'),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_tr',
            field=models.CharField(max_length=100, null=True, verbose_name='описания'),
        ),
    ]
