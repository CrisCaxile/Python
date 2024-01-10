from django.shortcuts import render


# Create your views here.

def index(request):
    """Página principal do projeto"""
    return render(request, 'projeto/index.html')