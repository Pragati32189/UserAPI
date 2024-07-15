# from django.shortcuts import render
# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer
# # Create your views here.

# class UserListCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.utils.dateparse import parse_datetime

@csrf_exempt
def all_user(request):
    if request.method == "GET":
        users = User.objects.all()
        users_list = list(users.values())
        return JsonResponse(users_list, safe=False)
    

@csrf_exempt
def one_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({"Error":"User not exist"}, status = 404)
    
    if request.method == 'GET':
        user_data = {
            'id':user.id,
            'username':user.username,
            'useraddress':user.useraddress,
            'isActive':user.isActive,
            'dateTimeModified':user.dateTimeModified
        }
        return JsonResponse(user_data)
    

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                username =data['username'],
                useraddress = data['useraddress'],
                isActive=data['isActive'],
                dateTimeModified = parse_datetime(data['dateTimeModified']) if 'dateTimeModified' in data else None
            )
            return JsonResponse({
                'id':user.id,
                'username':user.username,
                'useraddress':user.useraddress,
                'isActive':user.isActive,
                'dateTimeModified':user.dateTimeModified
            }, status=201)
        except KeyError:
            return JsonResponse({"Error":str(KeyError)}, status=400)
        

@csrf_exempt
def user_update(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        return JsonResponse({"Error":"User not exist"}, status = 404)
    

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            user.username =data.get('username' , user.username),
            user.useraddress = data.get('useraddress', user.useraddress),
            user.isActive=data.get('isActive') if isinstance(data['isActive'], bool) else user.isActive
            user.dateTimeModified = parse_datetime(data.get('dateTimeModified')) if 'dateTimeModified' in data else None
            user.save()
            return JsonResponse({
                'id':user.id,
                'username':user.username,
                'useraddress':user.useraddress,
                'isActive':user.isActive,
                'dateTimeModified':user.dateTimeModified
            })
        except KeyError:
            return JsonResponse({"Error":str(KeyError)}, status=400)
        

@csrf_exempt
def user_delete(request,id):
    try:
        user = User.objects.get(id=id)
    except:
        return JsonResponse({"Error":f"User not exist with id {id}"}, status = 404)

    
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message':f'User deleted successfully {user.username}'}, status=204)