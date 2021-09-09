from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

import datetime

START_YEAR_CHOICES = [str(num) for num in range(1970, datetime.datetime.now().year+1)]

class ProfileForm(forms.ModelForm):
    coding_start_date = forms.DateField(widget = forms.SelectDateWidget(years=START_YEAR_CHOICES))
    class Meta:
        model = Profile
        exclude = ['owner', 'user_name', 'solved_count', 'group_id', 'group_reader']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'placeholder': 'Add  %s' % name}
            )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class' : 'input', 'placeholder' : 'Add %s' % name})

class AlgorithmForm(forms.ModelForm):
    class Meta:
        model = Algorithm
        exclude = ['profile_id']
    
    def __init__(self, *args, **kwargs):
        super(AlgorithmForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'placeholder': 'Add %s' % name})