from django import forms

from .models import *

class StudyGroupForm(forms.ModelForm):
  class Meta:
    model = StudyGroup
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(StudyGroupForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update(
        {'class': 'input', 'placeHolder': 'Add %s' % name})