from django.shortcuts import render

def peticiones(request):
    return render(request, 'peticiones_admin/peticiones.html')
