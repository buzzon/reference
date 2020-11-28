from django.urls import path

from . import views

app_name = 'core-api'
urlpatterns = [
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('board/', views.BoardList.as_view(), name='board-list'),
    path('board/<slug:slug>/', views.BoardDetail.as_view(), name='board-detail')
]
