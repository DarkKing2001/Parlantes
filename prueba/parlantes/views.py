from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    lista = Parlante.objects.all()
    context={'listado' : lista}
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
               return render(request, 'parlantes/errores/error_204.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

def boton_buscar(request):
    print("ok, estamos en la vista boton buscar")
    context={}
    return render(request, 'parlantes/crud/boton_buscar.html', context)

def buscar_por_nombre(request):
    print("hola  estoy en buscar_por_rut...")
    if request.method == 'POST':
       mi_nombre = request.POST['nombre']

       if mi_nombre != "":
           try:
               parlante = Parlante()
               parlante = Parlante.objects.get(nombre=mi_nombre)
               if parlante is not None:
                   print("Parlante=", parlante)
                   context={'parlante': parlante}
                   return render(request, 'parlantes/crud/mostrar_datos.html', context)
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

def eliminar(request):
    print("ok, estamos en la vista eliminar")
    context={}
    return render(request, 'parlantes/crud//boton_eliminar.html', context)

def eliminar_por_nombre(request):
    print("hola  estoy en eliminar_por_nombre...")
    if request.method == 'POST':
       mi_nombre = request.POST['nombre']

       if mi_nombre != "":
           try:
               parlante = Parlante()
               parlante = Parlante.objects.get(nombre = mi_nombre)
               if parlante is not None:
                   print("Parlante=", parlante)
                   parlante.delete()
                   return render(request, 'parlantes/mensajes/parlante_eliminado.html', {})
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

def editar(request):
    print("ok, estamos en la vista editar")
    context = {}
    return render(request, 'parlantes/crud/boton_editar.html', context)

def editar_por_nombre(request):
    print("hola  estoy en editar_por_nombre...")
    if request.method == 'POST':
       mi_nombre = request.POST['nombre']

       if mi_nombre != "":
           try:
               parlante = Parlante()
               parlante = Parlante.objects.get(nombre = mi_nombre)
               if parlante is not None:
                   print("Parlante=", parlante)
                   context={'parlante': parlante}
                   return render(request, 'parlantes/crud/formulario_editar.html', context)
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

def actualizar_parlante(request):
    print("hola  estoy en actualizar_parlante...")
    if request.method == 'POST':

       mi_id     = request.POST['id_parlante']
       mi_nombre = request.POST['nombre']
       mi_tipo   = request.POST['tipo']
       mi_foto   = request.FILES['foto']

       if mi_nombre != "":
           try:
               parlante = Parlante()

               parlante.id_parlante = mi_id
               parlante.nombre = mi_nombre
               parlante.tipo = mi_tipo
               parlante.foto = mi_foto

               parlante.save()

               return render(request, 'parlantes/mensajes/dato_editado.html',{})

           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_204.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})