from msilib.schema import Class
from django.shortcuts import render, redirect 
from http.client import HTTPResponse
from django.http import HttpResponse

from Guarda.forms import ClassificacaoForm, obraForm, tipo_de_obraForm

from .models import obra
from .models import tipo_de_obra
from .models import Classificacao


# Create your views here.

def Read(request):
    data = {}
    
    data['obras'] = obra.objects.all()
    data['tipos_de_obras'] = tipo_de_obra.objects.all()
    data['Classificacoes'] = Classificacao.objects.all()
    return render(request, 'Read.html', data)

def Create(request):
    data = {}
    form = tipo_de_obraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form 
    return render(request, 'form.html', data)

def Create2(request):
    data = {}
    form = ClassificacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form
    return render(request, 'form.html', data)

def Create3(request):
    data = {}
    form = obraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    Tipo_de_obra = tipo_de_obra.objects.get(pk=pk)
    form = tipo_de_obraForm(request.POST or None, instance = Tipo_de_obra)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form
    data['tipo_de_obra'] = Tipo_de_obra
    return render(request, 'form.html', data)

def update2(request, pk):
    data = {}
    classificacao = Classificacao.objects.get(pk=pk)
    form = ClassificacaoForm(request.POST or None, instance = classificacao)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form
    data['classificacao'] = classificacao
    return render(request, 'form.html', data)

def update3(request, pk):
    data = {}
    Obra = obra.objects.get(pk=pk)
    form = obraForm(request.POST or None, instance = Obra)

    if form.is_valid():
        form.save()
        return redirect('url_Read')

    data['form'] = form
    data['obra'] = Obra
    return render(request, 'form.html', data)

def delete(request, pk):
    Tipo_de_obra = tipo_de_obra.objects.get(pk=pk)
    Tipo_de_obra.delete()

    return redirect('url_Read') 

def delete2(request, pk):
    classificacao = Classificacao.objects.get(pk=pk)
    classificacao.delete()

    return redirect('url_Read') 

def delete3(request, pk):
    Obra = obra.objects.get(pk=pk)
    Obra.delete()

    return redirect('url_Read') 

