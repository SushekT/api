from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from DemoAPI.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from django.contrib.auth.models import User

# Create your views here.
class Productset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    


@api_view(['POST'])
def signup(request):
    data = request.data
    user = User(email=data['email'], username=data['username'], )
    user.set_password(data['password1'])
    user.save()
    profile = Profile(user=user, name=data['name'], phone=data['phone'])
    profile.save()
    return JsonResponse({'token': 'sdjasndjkasd' },status=201)
       
@api_view(['POST'])
def login(request):

    data = request.data
    user = authenticate(request, username=data['username'], password=data['password'])

    if user is None:
        return JsonResponse({'error':'No user found'})
    else:
        return JsonResponse({'token': 'sdjasndjkasd' },status=201)