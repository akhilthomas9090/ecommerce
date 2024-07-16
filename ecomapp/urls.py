from django.urls import path
from ecomapp import views


urlpatterns = [
    path('base',views.about,name='base'),
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    
]
