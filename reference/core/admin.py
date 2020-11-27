from django.contrib import admin

from .models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created')


admin.site.register(Board, BoardAdmin)
