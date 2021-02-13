from django.db import models
from authentication.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255,null=False)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    