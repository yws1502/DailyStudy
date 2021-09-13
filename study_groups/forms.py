from django import forms

from .models import *

class StudyGroupForm(forms.ModelForm):
  class Meta:
    model = StudyGroup
    fields = '__all__'