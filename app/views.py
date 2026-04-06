from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView as ApiView
from django.shortcuts import get_object_or_404
from app.models import User, Role
from app.serializers import UserSerializer, RoleSerializer

class UserView(ApiView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    # MODIFICAR (PUT)
    def put(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # ELIMINAR (DELETE)
    def delete(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        usuario.delete()
        return Response(status=204)

class RoleView(ApiView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        role = get_object_or_404(Role, pk=pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        role = get_object_or_404(Role, pk=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    