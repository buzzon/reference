from rest_framework import viewsets

from core.api.serializers import *
from core.models import *


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = CardSerializer
