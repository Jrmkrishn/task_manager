# tasks/admin.py
from django.contrib import admin
from .models import Task
from .models import GoogleOAuthKey
from invitations.models import Invitation

admin.site.register(Task)


@admin.register(GoogleOAuthKey)
class GoogleOAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_secret', 'redirect_uri')


