from django.urls import path
from .views import photo_list,photo_blend


urlpatterns = [
    path('home/', photo_list, name="photo_list"),
    path('blend/', photo_blend, name="photo_blend"),
]