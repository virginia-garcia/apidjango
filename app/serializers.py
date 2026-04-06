from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'users']


class UserSerializer(serializers.ModelSerializer):
   
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'dni', 'birth_date', 'role', 'activo']