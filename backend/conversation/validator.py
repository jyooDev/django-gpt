from rest_framework import status
from rest_framework.response import Response

def validate_user(request_user, username):
    if request_user.username != username:
        return Response({"error": "You do not have permission to access this resource."}, status=status.HTTP_403_FORBIDDEN)
    return None
