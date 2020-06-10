from django.contrib import admin
from .models import Game
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator',)
    list_display_links = ('id', 'name', )
    list_filter = ('creator', )
    search_fields = ('name', )


admin.site.register(Game, GameAdmin)
