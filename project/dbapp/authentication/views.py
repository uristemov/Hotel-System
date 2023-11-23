


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  *
from .models import  *
from django.core.mail import send_mail


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    # send_mail("Hello", "My content","200103413@stu.sdu.edu.kz", ["200103413@stu.sdu.edu.kz", "200103158@stu.sdu.edu.kz"], fail_silently=False, html_message="<h1 style='color:red'>New user came!</h1>")
    

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            firstname = form.cleaned_data.get("first_name")
            email = form.cleaned_data.get("email")
            user = authenticate(username=username, password=password , first_name = firstname)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            send_mail("Trip Administration", "Welcome to website!","200103034@stu.sdu.edu.kz", [email], fail_silently=False, html_message="<h1 style='color:red'>New user came!</h1>")
            return redirect("/login/")
            

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


