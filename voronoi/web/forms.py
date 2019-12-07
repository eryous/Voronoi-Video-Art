from django import forms
from django.db import models
from .models import *


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
