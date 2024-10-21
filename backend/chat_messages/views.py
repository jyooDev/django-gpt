from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from conversation.models import Conversation
from .serializers import MessageSerializer
from .models import Message
from .validator import validate_user

class MessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, conversation_id):
        try:
            conversation = Conversation.objects.get(id = conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)
                
        validate_error = validate_user(request.user, conversation.username)
        if validate_error:
            return validate_error
        messages = Message.objects.filter(related_conversation=conversation).order_by('created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request, conversation_id):
        try:
            conversation = Conversation.objects.get(id = conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)
                
        validate_error = validate_user(request.user, conversation.username)
        if validate_error:
            return validate_error

        try:
            sender = request.data['sender']
            message_content = request.data['message_content']
        except KeyError:
            return Response({"error": "Key not found."}, status=status.HTTP_400_BAD_REQUEST)   
        serializer = MessageSerializer(
            data={'sender': sender,
                  'message_content': message_content,
                  'related_conversation': conversation}
        )        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)