from django.shortcuts import render
from .models import Genero,Alumnos

# Create your views here.
def index(request):
    alumnos = Alumnos.objects.all()#select * from
    context = {"alumnos": alumnos}
    print(alumnos)
    return render(request,"alumnos/index.html",context)

def index2(request):
    alumnos = Alumnos.objects.raw('SELECT * FROM alumnos_alumnos')
    context = {"alumnos":alumnos}
    return render(request,"alumnos/listadoSql.html",context)