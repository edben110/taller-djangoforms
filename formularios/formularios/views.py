from django.shortcuts import render


def home(request):
    """Vista principal con enlaces a ambos formularios."""
    return render(request, 'home.html')
