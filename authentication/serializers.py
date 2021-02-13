
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from rest_framework import serializers
from .models import User



class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure email is provided and is unique
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This email is already used by another user',
            )
        ],
        error_messages={
            'required': 'Email is required',
        }
    )

    password = serializers.RegexField(
        regex='',
        max_length=128,
        min_length=8,
        write_only=True,
        required=True,
        error_messages={
            'required': 'Password is required',
            'invalid': 'Password must have a number and a letter',
            'min_length': 'Password must have at least 8 characters',
            'max_length': 'Password cannot be more than 128 characters'
        }
    )
    username = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        min_length=4,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Username must be unique',
            )
        ],
        error_messages={
            'invalid': 'Make sure username is well structured',
            'required': 'Username is required',
            'min_length': 'Username must have at least 4 characters'
        }
    )
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token,
        }


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
