from django.urls import path
from .views import photo_list, photo_blend, photoView, photo_cartoonify

app_name="home"
urlpatterns = [
    path('', photo_list, name="photo_list"),
    path('blend/', photo_blend, name="photo_blend"),
    path('photos/', photoView, name="photoView"),
    path('cartoonify/<int:id>', photo_cartoonify, name="photo_cartoonify")
]