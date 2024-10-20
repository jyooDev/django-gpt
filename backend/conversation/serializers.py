from rest_framework.serializers import ModelSerializer
from .models import Conversation

class ConversationSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'username', 'title', 'title_slug', 'created_at')