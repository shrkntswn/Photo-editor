from PIL import Image
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
	x = forms.FloatField(widget= forms.hiddenInput())  
	y = forms.FloatField(widget= forms.hiddenInput())  
	width = forms.FloatField(widget= forms.hiddenInput())  
	height = forms.FloatField(widget= forms.hiddenInput()) 

	class Meta:
		model = Photo
		fields = ('file', 'x', 'y', 'width', 'height')

		def save(self):
			photo = super(PhotoForm, self).save()
			x = self.cleaned_data.get('x')
			y = self.cleaned_data.get('y')
			w = self.cleaned_data.get('width')
			h = self.cleaned_data.get('height')

			image = Image.open(photo.file)
			cropped_image = image.crop((x, y, w+x, h+y))
	        resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)
	        resized_image.save(photo.file.path)

	        return photo
