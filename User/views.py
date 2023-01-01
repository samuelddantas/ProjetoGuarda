from django.shortcuts   import render, redirect
from User               import models, forms

# ===============================
# CRUD - Assistido
# ===============================

def createAssistido(request):
    form = forms.AssistidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cAssistido")
    Assistidos = models.Assistido.objects.all()
    listagem = {
        'form_Assistido': form,
        'Assistidos_chave': Assistidos,
    }

    return render(request, "showAssistido.html", listagem)

def updateAssistido(request, id_Assistido):
    Assistido = models.Assistido.objects.get(pk=id_Assistido)
    form  = forms.AssistidoForm(request.POST or None, instance=Assistido)
    if form.is_valid():
        form.save()
        return redirect("cAssistido")
    listagem = {
        'form_Assistido': form,
    }
    return render(request, "showAssistido.html", listagem)

def deleteAssistido(request, id_Assistido):
    Assistido = models.Assistido.objects.get(pk=id_Assistido)
    Assistido.delete()
    return redirect("cAssistido")

# ===============================
# CRUD - Review
# ===============================

def createReview(request):
    form = forms.ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cReview")
    Reviews = models.Review.objects.all()
    listagem = {
        'form_Review': form,
        'Reviews_chave': Reviews,
    }

    return render(request, "showReview.html", listagem)

def updateReview(request, id_Review):
    Review = models.Review.objects.get(pk=id_Review)
    form  = forms.ReviewForm(request.POST or None, instance=Review)
    if form.is_valid():
        form.save()
        return redirect("cReview")
    listagem = {
        'form_Review': form,
    }
    return render(request, "showReview.html", listagem)

def deleteReview(request, id_Review):
    Review = models.Review.objects.get(pk=id_Review)
    Review.delete()
    return redirect("cReview")