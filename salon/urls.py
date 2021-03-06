"""salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include , re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from core.views import VerPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('',include('core.urls')),
    path('',include('pwa.urls')),
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve , {
            'document_root': settings.MEDIA_ROOT,
        })

    ]

admin.site.site_header = "Administración Paola Toledo"
admin.site.index_title = "Modulos de administración"
admin.site.site_title = "Paola Toledo Salon de Belleza Integral"