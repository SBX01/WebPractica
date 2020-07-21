from django.urls import path , include
from .views import Home, Agendar,Blog , VerPost
from django.conf.urls import url


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    path('blog/', Blog, name="blog"),
    path('',include('pwa.urls')),
    url(r'^blog/(?P<slug>[-\w]+)/$', VerPost.as_view() ),
]
