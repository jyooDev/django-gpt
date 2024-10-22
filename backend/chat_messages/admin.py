from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('get_conversation_username', 'sender', 'message_content', 'created_at')

    search_fields = ('related_conversation__username__username', 'message_content')

    def get_conversation_username(self, obj):
        return obj.related_conversation.username

    get_conversation_username.short_description = 'Conversation Username'
