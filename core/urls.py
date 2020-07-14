from django.urls import path , include
from .views import Home, Agendar


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    path('',include('pwa.urls')),
]
