from rest_framework import serializers
from .models import  Credentials, Ratings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import pdb


class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ('id','name','url', 'username', 'password', 'number_of_ratings', 'avg_rating')

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'credential','user','stars')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}






