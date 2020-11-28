from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import *


class BoardForUserSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'url']
        extra_kwargs = {
            'id': {'read_only': False}
        }


class UserSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    boards = BoardForUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'password', 'boards']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)

        new_boards = validated_data.pop('boards', {})
        for board in new_boards:
            if 'id' in board:
                card_id = board.get('id')
                board.pop('id')
                Board.objects.update_or_create(
                    id=card_id,
                    defaults={'User': instance, **board},
                )
            else:
                Board.objects.create(owner=instance, **board)
        instance.save()
        return instance

    @staticmethod
    def get_boards(obj):
        boards_url = []
        for board in Board.objects.filter(owner=obj.id):
            boards_url.append(board.get_absolute_url())
        return boards_url


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'deadline', 'preliminaryTime', 'totalTime', 'updated',
                  'positionX', 'positionY']
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }


class BoardSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    owner = serializers.URLField(source='get_owner_absolute_url', read_only=True)
    cards = CardSerializer(required=False, many=True)

    class Meta:
        model = Board
        fields = ['url', 'title', 'owner', 'created', 'cards']

    def create(self, validated_data):
        cards_data = validated_data.pop('cards', [])
        board = Board.objects.create(**validated_data)
        for card in cards_data:
            Card.objects.create(board=board, **card)
        return board

    def update(self, instance, validated_data):
        new_card = validated_data.pop('cards', {})
        instance.title = validated_data.get('title', instance.title)

        for card in new_card:
            if 'id' in card:
                card_id = card.get('id')
                card.pop('id')
                Card.objects.update_or_create(
                    id=card_id,
                    defaults={'Board': instance, **card},
                )
            else:
                Card.objects.create(board=instance, **card)
        instance.save()
        return instance


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'
