from django.urls import path
from .models import Album, Photo
from . import views
from django.views.generic import ListView, DetailView

app_name = 'photo'
urlpatterns = [
    path('', ListView.as_view(model=Album), name='index'),
    path('album', ListView.as_view(model=Album), name='album_list'),
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),
    path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),

    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),
    path('album/<int:pk>/update/',
         views.AlbumPhotoUV.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),
    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),
    path('photo/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),

]
