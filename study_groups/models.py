from django.db import models

from uuid import uuid4
# Create your models here.

class StudyGroup(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True)
  group_image = models.ImageField(
    upload_to='study_groups/', default='study_groups/default.jpg', null=True, blank=True)
  goal = models.CharField(max_length=500, null=True, blank=True)
  penalty = models.CharField(max_length=500, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

  def __str__(self):
    return self.name