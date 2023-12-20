from django.contrib import admin

from . import models


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "user",
        "status",
        "contact_info",
        "created",
        "updated",
    ]


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Status)
