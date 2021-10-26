from django.urls import path
from .views import PostViewset


urlpatterns = [
path('', PostViewset, name='api_view'),
]
