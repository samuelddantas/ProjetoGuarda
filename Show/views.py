from django.shortcuts           import render, redirect
from Show                       import forms, models
from User                       import models as UserModels
from django.contrib.auth.models import User

def index(request):
    user = User.objects.filter(id=request.user.id).first()

    obras = models.Obra.objects.all()
    if user:
        reviews = UserModels.Review.objects.filter(rev_use_id=user.id)
    else:
        reviews = None

    listagem = {
        'obras': obras,
        'reviews': reviews,
    }
    return render(request, "index.html", listagem)

# ===============================
# CRUD - Mídia
# ===============================

def createMidia(request):
    form = forms.MidiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    midias = models.Midia.objects.all()
    listagem = {
        'form_midia': form,
        'midias_chave': midias,
    }

    return render(request, "showMidia.html", listagem)

def updateMidia(request, id_midia):
    midia = models.Midia.objects.get(pk=id_midia)
    form  = forms.MidiaForm(request.POST or None, instance=midia)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {
        'form_midia': form,
    }
    return render(request, "showMidia.html", listagem)

def deleteMidia(request, id_midia):
    midia = models.Midia.objects.get(pk=id_midia)
    midia.delete()
    return redirect("main")

# ===============================
# CRUD - Gênero
# ===============================

def createGenero(request):
    form = forms.GeneroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    generos = models.Genero.objects.all()
    listagem = {
        'form_genero': form,
        'generos_chave': generos,
    }

    return render(request, "showGenero.html", listagem)

def updateGenero(request, id_genero):
    genero = models.Genero.objects.get(pk=id_genero)
    form  = forms.GeneroForm(request.POST or None, instance=genero)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {
        'form_genero': form,
    }
    return render(request, "showGenero.html", listagem)

def deleteGenero(request, id_genero):
    genero = models.Genero.objects.get(pk=id_genero)
    genero.delete()
    return redirect("main")

# ===============================
# CRUD - Obra
# ===============================

def createObra(request):
    form = forms.ObraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    Obras = models.Obra.objects.all()
    listagem = {
        'form_Obra': form,
        'Obras_chave': Obras,
    }

    return render(request, "showObra.html", listagem)

def updateObra(request, id_Obra):
    Obra = models.Obra.objects.get(pk=id_Obra)
    form  = forms.ObraForm(request.POST or None, instance=Obra)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {
        'form_Obra': form,
    }
    return render(request, "showObra.html", listagem)

def deleteObra(request, id_Obra):
    Obra = models.Obra.objects.get(pk=id_Obra)
    Obra.delete()
    return redirect("main")