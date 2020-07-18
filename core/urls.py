from django.urls import path , include
from .views import Home, Agendar,Blog


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    path('blog/', Blog, name="blog"),
    path('',include('pwa.urls')),
]
