from django.shortcuts import render

# Create your views here.
def introrecetas_view(request):
    return render(request, 'introducir_recetas/introrecetas.html')