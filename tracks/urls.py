from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music_list, name='music_list'),
    path('music/<int:id>/', views.music_detail, name='music_detail'),
    path('music/create/', views.music_create, name='music_create'),
    path('music/<int:id>/update/', views.music_update, name='music_update'),
    path('music/<int:id>/delete/', views.music_delete, name='music_delete'),
]
