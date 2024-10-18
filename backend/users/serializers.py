from rest_framework.serializers import ModelSerializer
from .models import ApplicationUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True}, 
            'last_name': {'required': True},
            }

    def create(self, validated_data):
        user = ApplicationUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user