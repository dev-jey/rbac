
from rest_framework import routers
from .views import *
# Specify a namespace
app_name="todo"

router = routers.DefaultRouter()
router.register(r'todo', TodoAPIViewSet, basename='todo')
urlpatterns = router.urls