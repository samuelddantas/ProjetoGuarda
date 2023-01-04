from django.shortcuts           import render, redirect
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.models import User
from User                       import models, forms

# ===============================
# Login e Registro
# ===============================

def loginUser(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username        = request.POST.get('username')
        password        = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main')
        else:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "login.html", erro)

def logoutUser(request):
    logout(request)
    return redirect('main')

def registerUser(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username        = request.POST.get('username')
        password        = request.POST.get('password')
        email           = request.POST.get('email')
        first_name      = request.POST.get('first_name')
        last_name       = request.POST.get('last_name')

        userVerify  = User.objects.filter(username=username).first()
        emailVerify = User.objects.filter(email=email).first()

        if userVerify:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "register.html", erro)

        if emailVerify:
            erro = {'erro': 'E-mail já está sendo utilizado.'}
            return render(request, "register.html", erro)

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()

        login(request, user)
        return redirect('main')

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
        return redirect("main")
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
        return redirect("main")
    listagem = {
        'form_Review': form,
    }
    return render(request, "showReview.html", listagem)

def deleteReview(request, id_Review):
    Review = models.Review.objects.get(pk=id_Review)
    Review.delete()
    return redirect("main")

# ===============================
# Read e Delete - User
# ===============================

def updateUser(request, id_User):
    user = User.objects.get(pk=id_User)
    form  = forms.UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {
        'form_User': form,
    }
    return render(request, "showUser.html", listagem)

def deleteUser(request, id_User):
    user = User.objects.get(pk=id_User)
    user.delete()
    return redirect("main")