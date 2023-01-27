from django.shortcuts           import render, redirect
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.models import User
from User                       import models, forms
from Show.models                import Obra

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
# CRUD - Review
# ===============================

def createReview(request):
    form = forms.ReviewForm(request.POST or None)
    user = User.objects.filter(id=request.user.id).first()
    if form.is_valid():
        review = models.Review.objects.create(
            rev_obr_id  = Obra.objects.get(obr_id=form['rev_obr_id'].value()),
            rev_use_id  = User.objects.get(id=user.id),
            rev_review  = form['rev_review'].value(),
            rev_nota    = form['rev_nota'].value(),
        )
        review.save()
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