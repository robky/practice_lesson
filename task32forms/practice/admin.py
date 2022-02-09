from django.contrib import admin
from .models import CD


class CDAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "genre")
    empty_value_display = "-пусто-"
    list_filter = ("genre",)


admin.site.register(CD, CDAdmin)