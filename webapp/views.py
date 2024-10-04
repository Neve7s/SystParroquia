import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from Purisima import settings
from webapp.forms import *


# Create your views here.
def home(request):
   return render(request, 'pages/index.html')


def loginapp(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UsuarioLoginForm()
    return render(request, 'pages/login.html', {'form': form})


def registerapp(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UsuarioCreationForm()
    return render(request, 'pages/register.html', {'form': form})


@login_required
def confirm(request):
    confirms = Confirmacion.objects.order_by('id')
    return render(request, 'pages/confirmacion/viewConfirm.html', {'confirms': confirms})


# Vista para agregar confirmación
def addConfirm(request):
    if request.method == 'POST':
        form = ConfirmacionForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar un mensaje de éxito
            return render(request, 'pages/confirmacion/addConfirm.html', {
                'form': form,
                'success_message': 'Confirmación guardada exitosamente.'
            })
    else:
        form = ConfirmacionForm()

    return render(request, 'pages/confirmacion/addConfirm.html', {'form': form})


# Vista para editar y "print" confirmación
@login_required
def printConfirm(request, id):
    confirmac = get_object_or_404(Confirmacion, pk=id)

    if request.method == 'POST':
        formaConfirm = ConfirmacionForm(request.POST, instance=confirmac)
        if formaConfirm.is_valid():
            formaConfirm.save()
            # Aquí también puedes mostrar un mensaje de éxito tras editar
            return render(request, 'pages/confirmacion/printConfirm.html', {
                'formaConfirm': formaConfirm,
                'success_message': 'Confirmación actualizada exitosamente.'
            })
    else:
        formaConfirm = ConfirmacionForm(instance=confirmac)

    return render(request, 'pages/confirmacion/printConfirm.html', {'formaConfirm': formaConfirm})


@login_required
def listar_confirmacion(request):
    confirms = Confirmacion.objects.all()

    # Obtener los valores del filtro
    nombre = request.GET.get('nombre', '')
    ano_confirmacion = request.GET.get('ano_confirmacion', '')

    # Aplicar los filtros
    if nombre:
        confirms = confirms.filter(nombre__icontains=nombre)

    if ano_confirmacion:
        confirms = confirms.filter(fecha__year=ano_confirmacion)

    return render(request, 'pages/confirmacion/viewConfirm.html', {'confirms': confirms})


@login_required
def delConfirm(request, id):
    confirma = get_object_or_404(Confirmacion, pk=id)
    if confirma:
        confirma.delete()
    return redirect('confirm')


# Matrimonio
@login_required
def matrimonio(request):
    matris = Matrimonio.objects.order_by('id')
    return render(request, 'pages/matrimonio/viewMatrimonio.html', {'matris': matris})


@login_required
def addMatrimonio(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/matrimonio/addMatrimonio.html', {'form': form})
    else:
        form = MatrimonioForm()
    return render(request, 'pages/matrimonio/addMatrimonio.html', {'form': form})


@login_required
def printMatrimonio(request, id):
    matrim = get_object_or_404(Matrimonio, pk=id)
    if request.method == 'POST':
        form = MatrimonioForm(request.POST, instance=matrim)
        if form.is_valid():
            form.save()
            return render(request, 'pages/matrimonio/printMatrimonio.html', {'form': form})
    else:
        form = MatrimonioForm(instance=matrim)
    return render(request, 'pages/matrimonio/printMatrimonio.html', {'form': form})


@login_required
def listar_matrimonios(request):
    matris = Matrimonio.objects.all()

    esposos = request.GET.get('esposos', '')
    ano_matrimonio = request.GET.get('ano_matrimonio', '')

    if esposos:
        matris = matris.filter(esposo__icontains=esposos) | matris.filter(esposa__icontains=esposos)

    if ano_matrimonio:
        matris = matris.filter(fecha_matrimonio__year=ano_matrimonio)

    return render(request, 'pages/matrimonio/viewMatrimonio.html', {'matris': matris})


@login_required
def delMatrimonio(request, id):
    matrimo = get_object_or_404(Matrimonio, pk=id)
    if matrimo:
        matrimo.delete()
    return redirect('matrimonio')


# Bautizo
@login_required
def bautizo(request):
    bautizos = Bautizo.objects.order_by('id')
    return render(request, 'pages/bautizos/viewBautizo.html', {'bautizos': bautizos})


@login_required
def addBautizo(request):
    if request.method == 'POST':
        form = BautizoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/bautizos/addBautizo.html', {'form': form})
    else:
        form = BautizoForm()
    return render(request, 'pages/bautizos/addBautizo.html', {'form': form})


@login_required
def printBautizo(request, id):
    bautizo = get_object_or_404(Bautizo, pk=id)
    if request.method == 'POST':
        formaBautizo = BautizoForm(request.POST, instance=bautizo)
        if formaBautizo.is_valid():
            formaBautizo.save()
            return render(request, 'pages/bautizos/printBautizo.html', {'formaBautizo': formaBautizo})
    else:
        formaBautizo = BautizoForm(instance=bautizo)
    return render(request, 'pages/bautizos/printBautizo.html', {'formaBautizo': formaBautizo})

@login_required
def listar_bautizos(request):
    bautizos = Bautizo.objects.all()

    # Obtener los valores del filtro
    apellidos_nombres = request.GET.get('nombre', '')
    ano_nacimiento = request.GET.get('ano_nacimiento', '')
    ano_bautizo = request.GET.get('ano_bautizo', '')

    # Aplicar los filtros
    if apellidos_nombres:
        bautizos = bautizos.filter(apellidos__icontains=apellidos_nombres) | bautizos.filter(nombres__icontains=apellidos_nombres)

    if ano_nacimiento:
        bautizos = bautizos.filter(fecha_nacimiento__year=ano_nacimiento)

    if ano_bautizo:
        bautizos = bautizos.filter(fecha_bautizo__year=ano_bautizo)

    return render(request, 'pages/bautizos/viewBautizo.html', {'bautizos': bautizos})


@login_required
def delBautizo(request, id):
    bautizo = get_object_or_404(Bautizo, pk=id)
    if bautizo:
        bautizo.delete()
    return redirect('bautizo')


def pricomunion(request):
    comunions = priComunion.objects.order_by('id')
    return render(request, 'pages/pricomunion/viewComunion.html', {'comunions': comunions})


@login_required
def addComunion(request):
    if request.method == 'POST':
        form = ComunionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/pricomunion/addComunion.html', {'form': form})
    else:
        form = ComunionForm()
    return render(request, 'pages/pricomunion/addComunion.html', {'form': form})


@login_required
def printComunion(request, id):
    comunion = get_object_or_404(priComunion, pk=id)
    if request.method == 'POST':
        form = ComunionForm(request.POST, instance=comunion)
        if form.is_valid():
            form.save()
            return render(request, 'pages/pricomunion/printComunion.html', {'form': form})
    else:
        form = ComunionForm(instance=comunion)
    return render(request, 'pages/pricomunion/printComunion.html', {'form': form})


@login_required
def listar_comunion(request):
    comunions = priComunion.objects.all()

    # Obtener los valores del filtro
    nombre = request.GET.get('nombre', '')
    ano_comunion = request.GET.get('ano_comunion', '')

    # Aplicar los filtros
    if nombre:
        comunions = comunions.filter(nombre__icontains=nombre)

    if ano_comunion:
        comunions = comunions.filter(fecha__year=ano_comunion)

    return render(request, 'pages/pricomunion/viewComunion.html', {'comunions': comunions})


@login_required
def delComunion(request, id):
    comuni = get_object_or_404(priComunion, pk=id)
    if comuni:
        comuni.delete()
    return redirect('pricomunion')


@login_required
def otros(request):
    return render(request, 'pages/Otros/otros.html')


@login_required
def export_db(request):
    # Ruta de la base de datos
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    # Leer el archivo de la base de datos
    with open(db_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/x-sqlite3')
        response['Content-Disposition'] = 'attachment; filename="db.sqlite3"'
        return response


def logoutapp(request):
    logout(request)
    return redirect('home')