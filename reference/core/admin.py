from django.contrib import admin

from .models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created')
    fields = ('title', 'owner')


admin.site.register(Board, BoardAdmin)
