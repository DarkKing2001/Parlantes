from django.shortcuts import render

# Create your views here.
def base(requeest):
    print("Estamos en la vista base..")
    context = {}
    return render(requeest, 'parlantes/base.html', context)

def inicio(requeest):
    print("Estamos en la vista inicio..")
    context = {}
    return render(requeest, 'parlantes/index.html', context)

def parlantes(requeest):
    print("Estamos en la vista parlantes..")
    context = {}
    return render(requeest, 'parlantes/tipoParlantes.html', context)