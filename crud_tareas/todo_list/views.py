from django.shortcuts import render , redirect
from django.http import HttpResponse
#importamos el formulario

from .forms import TodoForm
from .models import TodoList


def create_todo(request):

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tareas')

    ctx = {
        'form':form,
        'value':'CREAR'
    }   
    return render(request, 'todo_templates/todo.html',ctx)



def edit_todo(request,id):
    '''
    Genera un render dependiendo del formulario
    '''
    # busco por medio del id

    tarea = TodoList.objects.get(id=id)
    form = TodoForm(instance=tarea)


    if request.method == 'POST':
        form = TodoForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/tareas')


    return render(request,'todo_templates/todo.html',{'form':form, 'value':'EDITAR'})


def delete_todo(request,id):
    tarea = TodoList.objects.get(id = id)

    if request.method == "POST":
        tarea.delete()
        return redirect('/tareas')
    ctx = {
        'tarea':tarea
    }

    return render(request, 'todo_templates/delete.html', ctx)