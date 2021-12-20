from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import akbar


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(akbar, BlogAdmin)
