from django.contrib import admin

from core.logs.models import SiteLog


class SiteLogAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'text',)


admin.site.register(SiteLog, SiteLogAdmin)
