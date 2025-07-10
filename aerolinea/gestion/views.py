from django.shortcuts import render

# Create your views here.
def home(request):
    """Vista de la página de inicio"""
    return render(request, 'gestion/home.html')
