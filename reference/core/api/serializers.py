from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='core-api:board-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'boards']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CardSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), write_only=True)

    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'deadline', 'preliminaryTime', 'totalTime', 'updated',
                  'positionX', 'positionY', 'board']
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='core-api:user-detail')
    cards = CardSerializer(required=False, many=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'created', 'owner', 'cards']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, validated_data):
        cards_data = validated_data.pop('cards')
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

        return instance


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'
