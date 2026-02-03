from django.shortcuts import render

def login(request):
    return render(request, 'registro_usuarios/regusers.html')
