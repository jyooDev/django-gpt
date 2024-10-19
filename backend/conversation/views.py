from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from .serializers import ConversationSerializer
from rest_framework.permissions import IsAuthenticated
from .validator import validate_user

class UserConversationListView(APIView):
    permission_classes = [IsAuthenticated]
        
    def get(self, request, username):
        validate_error = validate_user(request.user, username)
        if validate_error:
            return validate_error

        conversations = Conversation.objects.filter(username = username)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
    
    def post(self, request, username):
        permission_classes = [IsAuthenticated]
    
        validate_error = validate_user(request.user, username)
        if validate_error:
            return validate_error

        try:
            title = request.data['title']
        except KeyError:
            return Response({"error": "Key not found."}, status=status.HTTP_400_BAD_REQUEST)   
        serializer = ConversationSerializer(
            data={'title': title,
                  'username': username}
        )        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserConversationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, title_slug):
        validate_error = validate_user(request.user, username)
        if validate_error:
            return validate_error

        try:
            conversation = Conversation.objects.get(username=username, title_slug=title_slug)
            serializer = ConversationSerializer(conversation)
            return Response(serializer.data)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, username, title_slug):
        try:
            Conversation.objects.get(username=username, title_slug=title_slug).delete()
            return Response(
                {"message": "Conversation is deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)