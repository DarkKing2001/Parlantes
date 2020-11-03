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

               parlante.nombre = mi_nombre
               parlante.tipo = mi_tipo
               parlante.foto = mi_foto

               parlante.save()

               return render(request, 'parlantes/mensajes/datos_grabados.html',{})

           except parlante.DoesNotExist:
               return render(request, 'parlantes/error/error_204.html', {})
       else:
           return render(request, 'parlantes/error/error_201.html', {})
    else:
        return render(request, 'parlantes/error/error_203.html', {})