from django.shortcuts import render


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


def our_story(request):
    """ A view to return the our story page. """

    return render(request, 'home/our_story.html')


def contact_us(request):
    """ A view to return the contact us page. """

    return render(request, 'home/contact_us.html')
