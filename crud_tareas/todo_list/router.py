from rest_framework import routers
from .viewsets import TodoViewSet

router = routers.SimpleRouter()

router.register('todo',TodoViewSet)
