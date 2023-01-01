from django.shortcuts import render, redirect
from Show             import forms, models

# ===============================
# CRUD - Mídia
# ===============================

def createMidia(request):
    form = forms.MidiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cMidia")
    midias = models.Midia.objects.all()
    listagem = {
        'form_midia': form,
        'midias_chave': midias,
    }

    return render(request, "templates/showMidia.html", listagem)

def updateMidia(request, id_midia):
    midia = models.Midia.objects.get(pk=id_midia)
    form  = forms.MidiaForm(request.POST or None, instance=midia)
    if form.is_valid():
        form.save()
        return redirect("cMidia")
    listagem = {
        'form_midia': form,
    }
    return render(request, "showMidia.html", listagem)

def deleteMidia(request, id_midia):
    midia = models.Midia.objects.get(pk=id_midia)
    midia.delete()
    return redirect("cMidia")

# ===============================
# CRUD - Gênero
# ===============================

def createGenero(request):
    form = forms.GeneroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cGenero")
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
        return redirect("cGenero")
    listagem = {
        'form_genero': form,
    }
    return render(request, "showGenero.html", listagem)

def deleteGenero(request, id_genero):
    genero = models.Genero.objects.get(pk=id_genero)
    genero.delete()
    return redirect("cGenero")

# ===============================
# CRUD - Obra
# ===============================

def createObra(request):
    form = forms.ObraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cObra")
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
        return redirect("cObra")
    listagem = {
        'form_Obra': form,
    }
    return render(request, "showObra.html", listagem)

def deleteObra(request, id_Obra):
    Obra = models.Obra.objects.get(pk=id_Obra)
    Obra.delete()
    return redirect("cObra")

# ===============================
# CRUD - Genero da Obra
# ===============================

def createGenero_da_Obra(request):
    form = forms.Genero_da_ObraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cGenero_da_Obra")
    Genero_da_Obras = models.Genero_da_Obra.objects.all()
    listagem = {
        'form_Genero_da_Obra': form,
        'Genero_da_Obras_chave': Genero_da_Obras,
    }

    return render(request, "showGenero_da_Obra.html", listagem)

def updateGenero_da_Obra(request, id_Genero_da_Obra):
    Genero_da_Obra = models.Genero_da_Obra.objects.get(pk=id_Genero_da_Obra)
    form  = forms.Genero_da_ObraForm(request.POST or None, instance=Genero_da_Obra)
    if form.is_valid():
        form.save()
        return redirect("cGenero_da_Obra")
    listagem = {
        'form_Genero_da_Obra': form,
    }
    return render(request, "showGenero_da_Obra.html", listagem)

def deleteGenero_da_Obra(request, id_Genero_da_Obra):
    Genero_da_Obra = models.Genero_da_Obra.objects.get(pk=id_Genero_da_Obra)
    Genero_da_Obra.delete()
    return redirect("cGenero_da_Obra")

# ===============================
# CRUD - Funcionario
# ===============================

def createFuncionario(request):
    form = forms.FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cFuncionario")
    Funcionarios = models.Funcionario.objects.all()
    listagem = {
        'form_Funcionario': form,
        'Funcionarios_chave': Funcionarios,
    }

    return render(request, "showFuncionario.html", listagem)

def updateFuncionario(request, id_Funcionario):
    Funcionario = models.Funcionario.objects.get(pk=id_Funcionario)
    form  = forms.FuncionarioForm(request.POST or None, instance=Funcionario)
    if form.is_valid():
        form.save()
        return redirect("cFuncionario")
    listagem = {
        'form_Funcionario': form,
    }
    return render(request, "showFuncionario.html", listagem)

def deleteFuncionario(request, id_Funcionario):
    Funcionario = models.Funcionario.objects.get(pk=id_Funcionario)
    Funcionario.delete()
    return redirect("cFuncionario")

# ===============================
# CRUD - Genero da Obra
# ===============================

def createFuncao(request):
    form = forms.FuncaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cFuncao")
    Funcaos = models.Funcao.objects.all()
    listagem = {
        'form_Funcao': form,
        'Funcaos_chave': Funcaos,
    }

    return render(request, "showFuncao.html", listagem)

def updateFuncao(request, id_Funcao):
    Funcao = models.Funcao.objects.get(pk=id_Funcao)
    form  = forms.FuncaoForm(request.POST or None, instance=Funcao)
    if form.is_valid():
        form.save()
        return redirect("cFuncao")
    listagem = {
        'form_Funcao': form,
    }
    return render(request, "showFuncao.html", listagem)

def deleteFuncao(request, id_Funcao):
    Funcao = models.Funcao.objects.get(pk=id_Funcao)
    Funcao.delete()
    return redirect("cFuncao")

# ===============================
# CRUD - Genero da Obra
# ===============================

def createProducao(request):
    form = forms.ProducaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cProducao")
    Producaos = models.Producao.objects.all()
    listagem = {
        'form_Producao': form,
        'Producaos_chave': Producaos,
    }

    return render(request, "showProducao.html", listagem)

def updateProducao(request, id_Producao):
    Producao = models.Producao.objects.get(pk=id_Producao)
    form  = forms.ProducaoForm(request.POST or None, instance=Producao)
    if form.is_valid():
        form.save()
        return redirect("cProducao")
    listagem = {
        'form_Producao': form,
    }
    return render(request, "showProducao.html", listagem)

def deleteProducao(request, id_Producao):
    Producao = models.Producao.objects.get(pk=id_Producao)
    Producao.delete()
    return redirect("cProducao")