from rest_framework import viewsets
from .serializer import TodoSerializer
from .serializer import TodoList

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer