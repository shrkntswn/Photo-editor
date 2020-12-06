from django.shortcuts import render, redirect, get_object_or_404
import cv2
from .forms import PhotoForm
from .models import Photo, PhotoBlend, Cartoonify
from django.conf import settings
import uuid
import os 

def get_file_name(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return filename

def photo_list(request):
	photos = Photo.objects.all().order_by('-uploaded_at')
	count = photos.count()
	outputs = PhotoBlend.objects.all().order_by('-id')
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
	fileName = settings.MEDIA_ROOT+ '/output/' + 'savedimage'+ str(uuid.uuid4()) +'.jpg'
	file = cv2.imwrite(fileName, img)
	output = PhotoBlend.objects.create(file=fileName)
	output.save()
	return redirect('home:photo_list')

def photoView(request):
	photos = Photo.objects.all().order_by('-uploaded_at')
	outputs = Cartoonify.objects.all().order_by('-id')
	return render(request, 'home/allPhotos.html', {'photos':photos, 'outputs':outputs})

def photo_cartoonify(request, id):
	photo = get_object_or_404(Photo, id=id)
	image = os.path.join(settings.BASE_DIR + '/' + photo.file.url)
	img =cv2.imread(image, 1)
	if request.method == 'GET':
		sigma_s = int(request.GET['slider1'])
		sigma_r = int(request.GET['slider2'])/100
		print("value is")
		print(sigma_s)
	cartoon_image = cv2.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
	#cartoon_image  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
	fileName = settings.MEDIA_ROOT+ '/output/' + 'cartoonImage' + str(uuid.uuid4()) +'.jpg'
	file = cv2.imwrite(fileName, cartoon_image)
	output = Cartoonify.objects.create(file=fileName)
	output.save()
	return redirect('home:photoView')

