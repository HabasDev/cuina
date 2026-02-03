from django.shortcuts import render

# Create your views here.
def regusers_view(request):
    return render(request, 'registro_usuarios/regusers.html')