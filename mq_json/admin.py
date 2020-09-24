from django.contrib import admin

from mq_json.models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['uuid']
    ordering = ['uuid']
    search_fields = ['uuid']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_uuid', 'recipient_uuid', 'message')
    ordering = ['sender_uuid']
    search_fields = ('sender_uuid', 'recipient_uuid')
