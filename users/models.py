from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class Profile(models.Model):
    # user infomation
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500)
    nick_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, unique=True, editable=False)
    short_intro = models.TextField(max_length=500, default='Hi there🖐')
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    # study group infomation
    solved_count = models.IntegerField(default=0, null=True, blank=True)
    group_id = models.CharField(max_length=200, null=True, blank=True)
    group_reader = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + '--' + self.user_name