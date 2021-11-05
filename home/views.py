from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page. """

    return render(request, 'home/index.html')


def lighting_inspiration(request):
    """ A view to return the lighting inspiration page. """

    return render(request, 'home/lighting_inspiration.html')


def dining_inspiration(request):
    """ A view to return the dining inspiration page. """

    return render(request, 'home/dining_inspiration.html')


def home_decor_inspiration(request):
    """ A view to return the home decor inspiration page. """

    return render(request, 'home/home_decor_inspiration.html')