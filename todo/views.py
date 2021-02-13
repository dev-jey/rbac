from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from permissions.permission import IsAdminUser, IsLoggedInUserOrAdmin
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import AllowAny

# Create your views here.

class TodoAPIViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action =='update':
            permission_classes  = [IsLoggedInUserOrAdmin]
        elif self.action == 'delete':
            permission_classes  = [IsAdminUser]
        elif self.action =='retrieve':
            permission_classes  = [IsLoggedInUserOrAdmin]
        elif self.action == 'create':
            permission_classes= [IsLoggedInUserOrAdmin]
        else:
            permission_classes = [IsAdminUser]
        import pdb; pdb.set_trace()
        return [permission() for permission in permission_classes]


