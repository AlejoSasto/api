from django.shortcuts import render, redirect
from .models import Project


# Create your views here.

def home(request):
    marca = Project.objects.all()
    return render(request, "Marcas.html", {"marca": marca})


def registrarMarca(request):
    id_marca = request.POST['txtid_marca']
    nombre = request.POST['txtNombre']
    activo = request.POST['txtActivo']
    item_ya_usado = request.POST['txtitem_ya_usado']

    project = Project.objects.create(id_marca=id_marca, nombre=nombre, activo=activo, item_ya_usado=item_ya_usado)
    return redirect('/')

def edicionMarca(request, id_marca):
    project = Project.objects.get(id_marca=id_marca)
    return render(request, "editarMarca.html", {'project':project})

def editarMarca(request):
    id_marca = request.POST['txtid_marca']
    nombre = request.POST['txtNombre']
    activo = request.POST['txtActivo']
    item_ya_usado = request.POST['txtitem_ya_usado']

    project = Project.objects.get(id_marca=id_marca)
    project.id_marca = id_marca
    project.nombre = nombre
    project.activo = activo
    project.item_ya_usado = item_ya_usado

    project.save()
    return redirect('/')

def eliminarMarca(request, id_marca):
    project = Project.objects.get(id_marca=id_marca)
    project.delete()
    return redirect('/')
