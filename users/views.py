from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserCreateSerializer, UserAuthSerializer, UserConfirmationSerializer
from .models import UserConfirmation

@api_view(["POST"])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id, 'detail': 'Пользователь зарегистрирован. Проверьте свой email для подтверждения.'})

@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = User.objects.get(username=serializer.validated_data['username'])
    user.is_active = True
    user.save()

    UserConfirmation.objects.filter(user=user).delete()
    return Response(status=status.HTTP_200_OK, data={'detail': 'Аккаунт подтвержден успешно.'})

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user:
        if not user.is_active:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'Аккаунт не подтвержден'})

        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'detail': 'Неверные учетные данные или Акканунт не подтверждён'})
