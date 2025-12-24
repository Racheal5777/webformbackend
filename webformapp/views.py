# from django.shortcuts import render


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserDetail
from .serializers import UserDetailSerializer
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

class UserDetailView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailListView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                token = Token.objects.get(key=token.split(' ')[1])
                user_details = UserDetail.objects.all()
                serializer = UserDetailSerializer(user_details, many=True)
                return Response(serializer.data)
            except Token.DoesNotExist:
                return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'No token provided'}, status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
