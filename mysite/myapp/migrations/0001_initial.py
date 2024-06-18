# Generated by Django 5.0.6 on 2024-06-18 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/img')),
                ('caption', models.CharField(max_length=100, verbose_name='описания')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hashtag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='follower', to='myapp.follow')),
                ('following', models.ManyToManyField(blank=True, related_name='following', to='myapp.follow')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='urer/img')),
                ('website', models.TextField()),
                ('followers', models.ImageField(blank=True, null=True, upload_to='')),
                ('nickname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='story/img')),
                ('video', models.FileField(blank=True, null=True, upload_to='story/video')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('creator', models.DateTimeField(auto_now_add=True)),
                ('members', models.ImageField(upload_to='')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
    ]
