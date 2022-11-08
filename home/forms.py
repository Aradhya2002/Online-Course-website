from .models import video
from django import forms

class Video_form(forms.ModelForm):
    class Meta:
        model=video
        fields=("caption", "video")
