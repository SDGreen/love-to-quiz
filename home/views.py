from django.shortcuts import render


# Create your views here.
def index(request):
    """index page for the site"""
    return render(request, 'home/index.html')
