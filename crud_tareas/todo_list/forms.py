# creando un formulario en base a un modelo

from django.forms import ModelForm
from .models import TodoList

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'