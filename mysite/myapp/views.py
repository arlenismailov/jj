from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, SearchFilter


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile
    serializer_class = UserProfileSerializer
    permission = [IsAuthenticated]


class FollowView(viewsets.ModelViewSet):
    queryset = Follow
    serializer_class = FollowSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post
    serializer_class = PostSerializer
    filter_backends = [ DjangoFilterBackend]
    filterset_fields = ['hashtag',]


class CommentLikeView(viewsets.ModelViewSet):
    queryset = Comment
    serializer_class = CommentSerializer


class StoryView(viewsets.ModelViewSet):
    queryset = Story
    serializer_class = StorySerializer


class GroupView(viewsets.ModelViewSet):
    queryset = Group
    serializer_class = GroupSerializer




