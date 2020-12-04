from django.shortcuts import render, redirect
import cv2

from .forms import PhotoForm
from .models import Photo, PhotoBlend
from django.conf import settings
import os

def photo_list(request):
	photos = Photo.objects.all().order_by('-uploaded_at')
	count = photos.count()
	outputs = PhotoBlend.objects.all()
	if request.method == 'POST':
		form = PhotoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home:photo_list')

	else:
		form = PhotoForm()
	return render(request, 'home/photo_list.html', {'form':form, 'photos':photos,'outputs':outputs,'count':count})


def photo_blend(request):
	photos = Photo.objects.all().order_by('-uploaded_at')[:2]
	image1= os.path.join(settings.BASE_DIR + '/' + photos[0].file.url)
	image2= os.path.join(settings.BASE_DIR+ '/' + photos[1].file.url)
	img1 = cv2.imread(image1, 1)
	img2 = cv2.imread(image2, 1)
	value1 = int(request.GET['slider1'])/100
	value2 = int(request.GET['slider2'])/100
	img = cv2.addWeighted(img1, value1, img2, value2, 0)
	fileName = settings.MEDIA_ROOT+ '/output/' + 'savedimage.jpg'
	file = cv2.imwrite(fileName, img)
	output = PhotoBlend.objects.all()
	output.delete()
	output = PhotoBlend.objects.create(file=fileName)
	output.save()
	return redirect('home:photo_list')

