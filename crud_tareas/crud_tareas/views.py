from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from todo_list.models import TodoList

# pagina de inicio!

# def landing_page(request):
#     now = datetime.now()
#     first_view = f'<h1> Hola desde Python-Django</h1> <p>{now}</p>'
#     return HttpResponse(first_view)

def pagina_inicio(request):

    # ==> request | plantillas | contexto
    return render(request,'index.html',{'nombre':'Anderson','hecho_por':'Django-Init'})

def noticias_page(request):
    return render(request,'noticias_page.html',{})

def todo_list(request):
    total_registros = TodoList.objects.count()
    tareas = TodoList.objects.all()


    return render(request,'todo_list.html',{'cantidad':total_registros, 'tareas':tareas})