from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, 'home.html')

#Formulario usuarios
def create(request):
    return render(request, 'create.html')

#inserção no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        
        data['msg'] = 'Usuario cadastrado com sucesso'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)


#Formulario painel
def painel(request):
    return render(request, 'painel.html')

#Formulario dologin
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Senha ou login incorretos'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html')

#Formulario dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

#Formulario logout
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Altera a senha
def pageChange(request):
    return render(request, 'changePass.html')
def changePassword(request):
    
    
    u = User.objects.get(email=request.user.email) 
    change = request.POST['password1']
    u.set_password(change)
    u.save()
    logout(request)
    return redirect('/painel/')

