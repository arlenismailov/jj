from django.urls import path
from .views import *


urlpatterns = [
    path('follow/', FollowView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('follow/<int:pk>/', FollowView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='follow_detail'),

    path('user/', UserProfileView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('user/<int:pk>/', UserProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='follow_detail'),

    path('post/', PostView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('post/<int:pk>/', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow_detail'),

    path('story/', StoryView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('story/<int:pk>/', StoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow_detail'),

    path('group/', GroupView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('group/<int:pk>/', GroupView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow_detail'),

    path('user/', UserProfileView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('user/<int:pk>/', UserProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow_detail'),

]
