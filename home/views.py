from django.shortcuts import render, redirect

from .forms import PhotoForm
from .models import Photo

def photo_list(request):
	photos = Photo.objects.all()
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('photo_list')

		else:
			form = PhotoForm()
		return render(request, 'home/photo_list.html')