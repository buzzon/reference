from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from core.models import *


def index(request):
    num_users = User.objects.count()
    num_boards = Board.objects.count()
    num_cards = Card.objects.count()
    num_components = Component.objects.count()

    if request.user.is_anonymous:
        board_list = None
    else:
        board_list = Board.objects.all().filter(owner=request.user)

    return render(
        request,
        'index.html',
        context={
            'num_users': num_users,
            'num_boards': num_boards,
            'num_cards': num_cards,
            'num_components': num_components,
            'board_list': board_list
        }
    )


class BoardDetail(generic.DetailView):
    model = Board
