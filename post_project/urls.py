"""post_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from api.views import PostViewset

router = routers.SimpleRouter()

router.register('post', PostViewset, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # for authentification management
    path('accounts/', include('accounts.urls')), #for sing up and auth app
    path('', include('posts.urls')), # to include urls.py from posts app
    #path('api/', include('api.urls')), # for the api DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
