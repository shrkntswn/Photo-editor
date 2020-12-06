from django.db import models
from django.urls import reverse


class Photo(models.Model):
	file = models.ImageField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
	

	def get_absolute_url(self):
		return reverse('home:photo_cartoonify', args=[self.id,])


class PhotoBlend(models.Model):
	file = models.ImageField(upload_to='media/output')


class Cartoonify(models.Model):
	file = models.ImageField(upload_to='media')
