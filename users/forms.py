from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

import datetime

START_YEAR_CHOICES = [str(num) for num in range(1970, datetime.datetime.now().year+1)]

# 각 클래스 메타안에 필드별 속성값을 커스터마이징 하는 함수
def update_widget(fields):
    for name, field in fields.items():
        field.widget.attrs.update(
            {'class': 'input', 'placeholder': 'Add %s' % name})

class ProfileForm(forms.ModelForm):
    coding_start_date = forms.DateField(widget = forms.SelectDateWidget(years=START_YEAR_CHOICES))
    class Meta:
        model = Profile
        exclude = ['owner', 'user_name', 'solved_count', 'group_id', 'is_leader']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        update_widget(self.fields)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        update_widget(self.fields)

class AlgorithmForm(forms.ModelForm):
    class Meta:
        model = Algorithm
        exclude = ['profile_id']
    
    def __init__(self, *args, **kwargs):
        super(AlgorithmForm, self).__init__(*args, **kwargs)
        update_widget(self.fields)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['is_read']
    
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        update_widget(self.fields)