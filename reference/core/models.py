from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Card(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    preliminaryTime = models.TimeField(null=True, blank=True)
    totalTime = models.TimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    positionX = models.IntegerField(default=0, blank=True)
    positionY = models.IntegerField(default=0, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cards')

    class Meta:
        ordering = ['updated']


class Component(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    preliminaryTime = models.TimeField(null=True, blank=True)
    totalTime = models.TimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    ordering = models.IntegerField(default=1, blank=True)
    executors = models.ManyToManyField('auth.User', related_name='components')
    cards = models.ForeignKey(Card, related_name='components', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['ordering', 'updated']
