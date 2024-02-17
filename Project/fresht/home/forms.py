from django import forms
from django.forms import ModelForm
from .models import *

class dump_user_info(ModelForm):
    class Meta:
        model=user_info
        fields="__all__"