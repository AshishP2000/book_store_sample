import logging

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

# Create your views here.

logging.basicConfig(filename='book_store.log', level=logging.INFO)


class UserRegister(APIView):
    def post(self, request):
        """
        register: getting user_name,email,password and phone from user and saving in the database
        request: data from user
        """
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'user is registered', 'status': 201, 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})


class UserLogin(APIView):
    def post(self, request):
        """
        login: getting user_name and password from user and logging
        request: data from user
        """
        try:
            user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if user is not None:
                return Response({'INFO': "LOGIN SUCCESSFUL", 'status': 202}, status=status.HTTP_202_ACCEPTED)
            return Response({'INFO': "LOGIN UNSUCCESSFUL", 'status': 401}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})

