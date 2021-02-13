from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from permissions.permission import IsAdminUser
# Create your views here.

class TodoAPIViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]