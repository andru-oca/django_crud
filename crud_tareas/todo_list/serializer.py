from rest_framework import serializers
from .models import TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        # que campos quiero traer?? en este caso los quiero todos
        fields = '__all__'
        # fields = [---> todos los campos en lista]

    