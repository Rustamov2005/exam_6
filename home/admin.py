from django.contrib import admin
from .models import Users, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'password')


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('comment', 'created', 'like')


