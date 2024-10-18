from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ApplicationUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
     
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated] 
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        
        # Ensure both passwords are provided
        if not current_password or not new_password:
            return Response({"error": "Both current and new password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the current password is correct
        if not user.check_password(current_password):
            return Response({"error": "Current password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Set the new password and save the user
        user.set_password(new_password)
        user.save()
        
        return Response({"success": "Password changed successfully."}, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    permission_classes = [] 

    def post(self, request):
        password = request.data.get("password")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    permission_classes = [] 

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
class UserDeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user 
        user.delete() 
        return Response({"message": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
