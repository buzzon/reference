from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from core.api.serializers import *
from core.models import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))


class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Board.objects.all().filter(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.all().filter(owner=self.request.user)

    def get_object(self):
        return get_object_or_404(Board, slug=self.kwargs.get('slug'))


class BoardDetailByPK(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.all().filter(owner=self.request.user)


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
