from django.shortcuts import render

# Create your views here.

from parlantes.models import Parlante

def base(requeest):
    print("Estamos en la vista base..")
    context = {}
    return render(requeest, 'parlantes/base.html', context)

def menu(requeest):
    print("Estamos en la vista menu..")
    context = {}
    return render(requeest, 'parlantes/index.html', context)

def tipo_parlante(requeest):
    print("Estamos en la vista tipo parlante..")
    context = {}
    return render(requeest, 'parlantes/tipoParlantes.html', context)

def agregar(request):
    print("ok, estamos en la vista agregarr")
    context={}
    return render(request, 'parlantes/crud/formulario_agregar.html', context)

def agregar_parlante(request):
    print("hola  estoy en agregar_parlante...")
    if request.method == 'POST':
       mi_nombre = request.POST['nombre']
       mi_tipo   = request.POST['tipo']
       mi_foto   = request.FILES['foto']

       if mi_nombre != "":
           try:
               parlante = Parlante()

               alumno.rut = mi_rut
               alumno.nombre = mi_nombre
               alumno.apellido_paterno = mi_paterno
               alumno.apellido_materno = mi_materno
               alumno.fecha_nacimiento = mi_fechaNac
               alumno.genero = mi_genero
               alumno.foto = mi_foto

               alumno.save()

               return render(request, 'personas/mensajes/datos_grabados.html',{})

           except alumno.DoesNotExist:
               return render(request, 'personas/error/error_204.html', {})
       else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})