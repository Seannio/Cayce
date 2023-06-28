from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('art/', views.ArtList.as_view(), name='art'),
    path('music/', views.MusicList.as_view(), name='music'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]