# Create your views here.

import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

logging.basicConfig(filename='book_store.log', level=logging.INFO)


class BookAPI(APIView):

    def post(self, request):
        """
        post: getting title,author,price,quantity,created_at from user and saving in the database
        request: data from user
        """
        try:
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Book is registered', 'status': 201, 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})

    def get(self, request):
        try:
            data = Book.objects.filter(id=request.data.get('id'))
            serializer = BookSerializer(data, many=True)
            print(serializer)
            return Response({'message': 'Book', 'status': 200, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})

    def put(self, request):
        """
        put: getting title,author,price,quantity,updated_at from user and saving in the database
        request: data from user
        """
        try:
            book_data = Book.objects.get(id=request.data.get('id'))
            serializer = BookSerializer(book_data, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Data is updated', 'status': 200, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})

    def delete(self, request):
        """
        post: getting id from user and deleting that book from database
        request: data from user
        """
        try:
            book_data = Book.objects.get(id=request.data.get('id'))
            book_data.delete()
            return Response({'message': 'Book deleted', 'status': 204},
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            logging.exception(ex)
            return Response({'message': str(ex)})
