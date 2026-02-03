from django.shortcuts import render

# Create your views here.

def faqs_view(request):
    return render(request, 'faqs/faqs.html') # <--- Aquí pones 'app/archivo.html'