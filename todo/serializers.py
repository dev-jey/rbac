from rest_framework import serializers
from .models import Todo
from authentication.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Todo
        fields = "__all__"
        # extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        return Todo.objects.create(**validated_data, created_by =self.context["request"].user )

