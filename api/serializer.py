from rest_framework import serializers
from .models import User

# Serializamos nuestro model para que pueda ser convertido en JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'nickName',
            'age',
            'is_active'
        ]
