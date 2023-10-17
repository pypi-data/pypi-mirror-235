from django.contrib import admin

from .models import Config


class ConfigAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "key",
        "value",
    ]
    search_fields = [
        "key",
        "value",
    ]


admin.site.register(Config, ConfigAdmin)
