from app.models import contacto
from django.shortcuts import render
from .forms import IngresaInfo
'''from django.conf import settings'''


# Create your views here.
def informacion(request):
    data ={
        'form': IngresaInfo()
    }

    if request.method == 'POST':
        formulario = IngresaInfo(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "info guardada"
        else:
            data["form"] = formulario
    return render(request, 'app/index.html', data)
    '''for i in range(0,1):
        formulario = Temperatura(nombre=input('ingrese su nombre:'), temperatura=input('ingresa t°:'))
        
        formulario.save()
    formulario = Temperatura.objects.values()
    context = {'formulario2': formulario}
    return render(request, 'app/agregar.html', context)'''

def producto(request):
    nombres = contacto.objects.all()

    data ={
        "nombres" : nombres
    }
    return render(request, 'app/agregar.html', data)


