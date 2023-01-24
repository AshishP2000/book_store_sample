import json
import logging

from django.http import JsonResponse

from .models import Registration

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
            user = Registration(user_name=data.get('user_name'), email=data.get('email'), password=data.get('password'),
                                phone=data.get('phone'))
            user.save()
            user_list = {'user_id': user.id, 'user_name': user.user_name, 'email': user.email,
                         'password': user.password, 'phone': user.phone}
            return JsonResponse({'data': user_list})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as ex:
        logging.exception(ex)


def show(request):
    try:
        if request.method == 'GET':
            print("d")
            data = Registration.objects.all().values()
            user_list = list(data)
            print(user_list)
            return JsonResponse({'data': user_list})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as ex:
        logging.exception(ex)


def login(request):
    """
    login: login user if user is present in database or not
    """
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            user = Registration.objects.filter(user_name=data.get('user_name'), password=data.get('password')).first()
            if user is not None:
                return JsonResponse({'Info': 'user logged in'})
            return JsonResponse({'Info': 'login unsuccessful'})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as ex:
        logging.exception(ex)
