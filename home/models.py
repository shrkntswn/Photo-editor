from django.db import models

class Photo(models.Model):
	file = models.ImageField()
	description = models.CharField(max_length=255, required=False)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class meta:
		verbose_name ='Photo'
		verbose_name_plural = 'photos'
