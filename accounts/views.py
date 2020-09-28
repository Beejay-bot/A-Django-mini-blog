from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email has already been registered')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('User created jareee')
                auto_login = auth.authenticate(username=username, password=password1)
                if auto_login is not None:
                    auth.login(request, auto_login)
                    messages.success(request, 'Login successful')
                    return redirect('/')
                else:
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match ')
            return render(request, 'signup.html')
    else:
        pass
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/')
    else:
        messages.error(request, "User doesn't exist")
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')

