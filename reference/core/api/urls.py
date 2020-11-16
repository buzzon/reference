from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'Board', views.BoardViewSet)
router.register(r'Component', views.ComponentViewSet)
router.register(r'Card', views.CardViewSet)

app_name = 'core-api'
urlpatterns = [
    url('', include(router.urls))
]
