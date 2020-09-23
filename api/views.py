from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Credentials, Ratings
from .serializers import CredentialsSerializer, RatingsSerializer, UserSerializer

class CredentialsViewSet(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )
    @action(detail=True, methods=['POST'])
    def rate_credential(self,request, pk=None):
        if 'stars' in request.data:
            stars = request.data['stars']
            user = request.user
            response = { 'message': 'it is working'}
            credential = Credentials.objects.get(id=pk);
            try:
                rating = Ratings.objects.get(user=user.id, credential=credential.id)
                rating.stars = stars
                rating.save()
                serializer =  RatingsSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
            except:
                rating = Ratings.objects.create(user=user, credential=credential, stars=stars)
                serializer = RatingsSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {"message": "you need to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def update(self, request, *args, **kwargs):
        response = {'message', 'You can\'t update a rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        response = {'message', 'You can\'t create a rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
