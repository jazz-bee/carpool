# we dont need the render
# from django.shortcuts import render
from users.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny

# from users.permissions.user import IsActiveUser
# TODO permissions: IsDriver, IsActiveUser, IsAdmin
# TODO ride permissions : IsRIdeOwner (puede modificar), IsPasssanger,

# Filters
# from rest_framework.filters import SearchFilter, OrderingFilter


# @api_view(['GET'])
# @permission_classes([AllowAny])
class UserList(generics.ListCreateAPIView):
    """
    Return a list of all the users
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    # only admins can request full list of users
    permissions_classes = [IsAdminUser]
    # permissions_classes = [AllowAny|IsAdminUSer] es un


# retrieveAPIView - Used for read-only endpoints to represent a single model instance.
# TODO ojo, solo el propio perfil
class UserDetail(generics.RetrieveAPIView):

    """
    Return self profile for the user making the request
    returns HTTP 404 Not Found if trying to get another user
    """
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    # permissions_classes = [IsActiveUser]
    # TODO agregar permiso IsActiveUser

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
