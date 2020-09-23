from django.contrib import admin
from .models import Credential
# Register your models here.


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ['name','url','username','password'];
    list_filter = ['name', 'url']
    search_fields = ['name','url', 'username', 'password']