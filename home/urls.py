from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lighting_inspiration/', views.lighting_inspiration, 
    name='lighting_inspiration'),
    path('dining_inspiration/', views.dining_inspiration, 
    name='dining_inspiration'),
    path('home_decor_inspiration/', views.home_decor_inspiration, 
    name='home_decor_inspiration'),
    path('our_story/', views.our_story, 
    name='our_story'),
    path('contact_us/', views.contact_us, 
    name='contact_us'),
]
