from django import forms
from .models import *


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ( 'first_name', 'last_name', 'background', 'about_featured', 'state', 'country', 'live_in', 'age', 'gender', 'profile_pic', )