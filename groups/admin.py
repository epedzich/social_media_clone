from django.contrib import admin
from . import models

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_filter = ['members']

    list_display = ['name', 'description']

    list_editable = ['description']

admin.site.register(models.Group, GroupAdmin)

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
