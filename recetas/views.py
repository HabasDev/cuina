from django.shortcuts import render

# Create your views here.
def recetas_view(request):
    return render(request, 'recetas/recetas.html')