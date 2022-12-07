from django.db import models

class TodoList(models.Model):
    '''
    este modelo va a ser quien nos permite crear una inicial base de datos de almacenaje de informacion
    '''
    class Meta:
        db_table ='todo_list'

    nombre = models.CharField(max_length=100 , unique=True )
    descripcion = models.TextField(max_length=300)
    horario_inicio = models.TimeField( blank=True , null= True)
    dia_realizar = models.DateField(blank=True , null= True)

    def __str__(self):
        return f'{self.nombre}'