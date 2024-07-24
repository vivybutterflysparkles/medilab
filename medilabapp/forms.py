from django import forms
from medilabapp.models import Appointment
from medilabapp.models import ImageModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department','doctor','message']

class ImageUploadForm(forms.ModelForm):
        class Meta:
            model = ImageModel
            fields = ['image', 'title', 'price']
