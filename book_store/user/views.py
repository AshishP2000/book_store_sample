import json
import logging

from django.contrib.auth import authenticate
from django.http import JsonResponse

from .models import User

# Create your views here.

logging.basicConfig(filename='book_store.log', level=logging.INFO)


def register(request):
    """
    register: getting user_name,email,password and phone from user and saving in the database
    request: data from user
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user = User.objects.create_user(username=data.get('username'), password=data.get('password'),
                                            first_name=data.get('first_name'), last_name=data.get('last_name'),
                                            email=data.get('email'))
            user_list = {'user_id': user.id, 'username': user.username, 'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email}
            return JsonResponse({'data': user_list})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as ex:
        logging.exception(ex)
        return JsonResponse({'message': str(ex)})


def login(request):
    """
    login: getting user_name and password from user and logging
    request: data from user
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                return JsonResponse({'INFO': "LOGIN SUCCESSFUL"})
            return JsonResponse({'INFO': "LOGIN UNSUCCESSFUL"})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as ex:
        logging.exception(ex)
        return JsonResponse({'message': str(ex)})
