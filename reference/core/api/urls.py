from django.urls import path

from . import views

app_name = 'core-api'
urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('boards/', views.BoardList.as_view(), name='board-list'),
    path('boards/<int:pk>/', views.BoardDetail.as_view(), name='board-detail'),
    # path('cards/', views.CardList.as_view(), name='card-list'),
    # path('cards/<int:pk>/', views.CardDetail.as_view(), name='card-detail'),
]
