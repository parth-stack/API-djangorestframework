from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    def create(self,data):
        user = User.objects.create(username=data['username'],email=data['email'],password=data['password'])
        return user

    def ask(self,data):
        user = User.objects.filter(username=data['username'],password=data['password']).first()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')