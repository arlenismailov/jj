from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from rest_framework.permissions import IsAuthenticated


class UserProfile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to='urer/img', null=True, blank=True)
    website = models.TextField()
    followers = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.nickname}'


class Follow(models.Model):
    followers = models.ManyToManyField('self', related_name='follower',blank=True)
    following = models.ManyToManyField('self', related_name='following',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/img', null=True, blank=True)
    caption = models.CharField(max_length=100, verbose_name='описания')
    created_at = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(UserProfile, blank=True, related_name='post_like')
    hashtag = models.TextField()


class PostLike(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # likes = models.OneToOneRel(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_like')


class CommentLike(models.Model):
    user = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Story(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story/img', null=True, blank=True)
    video = models.FileField(upload_to='story/video', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # expires_at


class Group(models.Model):
    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    creator = models.DateTimeField(auto_now_add=True)
    members = models.ImageField()
    # join_key = models.
#
# CRUD
# FILTER(hashtag)
# search(nickname)
# permission(IsAuthOrReadOn)
# register + google + github
# ru
# en...
# github
