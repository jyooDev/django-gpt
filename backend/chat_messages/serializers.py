from rest_framework.serializers import ModelSerializer
from .models import Message

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'message_content','related_conversation', 'created_at')