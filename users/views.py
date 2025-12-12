from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created", "data": serializer.data})
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_user(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User updated", "data": serializer.data})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return Response({"message": "User deleted"})