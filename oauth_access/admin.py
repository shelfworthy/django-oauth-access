from django.contrib import admin

from .models import UserAssociation

class UserAssociationAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'identifier']

admin.site.register(UserAssociation, UserAssociationAdmin)