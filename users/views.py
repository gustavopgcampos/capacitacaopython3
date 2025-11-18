from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def register (request):

    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        emailExists = User.objects.filter(email=email).first()
    
        if emailExists: 
            return render(request, 'login.html', {
                'login_error': 'E-mail já está em uso.'
            })
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')

def login (request): 

    if request.method == "GET": 
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user: 
            login_django(request, user)

            return redirect('biblioteca:home')
        else: 
            return render(request, 'login.html', {
                'login_error': 'Email ou Senha Inválidos.'
            })