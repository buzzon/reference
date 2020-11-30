from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'board/<slug:slug>/', views.BoardDetail.as_view(), name='board-detail'),
    path(r'card/<int:pk>/', views.BoardDetail.as_view(), name='card-detail')
]
