from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home/index.html') # Cuando alguien accede al Home carga el archivo HTML