from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import UserConfirmation

class BaseUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, max_length=150, required=True)

class UserCreateSerializer(BaseUserSerializer):
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=False
        )
        confirmation = UserConfirmation.objects.create(user=user)
        confirmation.generate_confirmation_code()
        return user

class UserAuthSerializer(BaseUserSerializer):
    pass

class UserConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')

        try:
            user = User.objects.get(username=username)
            confirmation = UserConfirmation.objects.get(user=user)
        except User.DoesNotExist:
            raise ValidationError("Пользователь не найден")
        except UserConfirmation.DoesNotExist:
            raise ValidationError("Код подтверждения не найден.")

        if confirmation.confirmation_code != confirmation_code:
            raise ValidationError("Неверный код подтверждения.")
        
        return data
