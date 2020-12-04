from django.db import models

class Photo(models.Model):
	file = models.ImageField()
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class meta:
		verbose_name ='Photo'
		verbose_name_plural = 'photos'

		def photoCount(self):
			return self.file.count()

class PhotoBlend(models.Model):
	file = models.ImageField(upload_to='media/output')
