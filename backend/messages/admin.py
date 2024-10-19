from django.contrib import admin
from models import Message
# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "message")
    search_fields=(
        "payload",
        "^conversation__username"
    )


    def get_username(self, obj):
        return obj.conversation.username
    
    get_username.short_description = 'Username'