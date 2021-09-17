from django.db import models
from django.contrib.auth.models import User

from study_groups.models import *
from uuid import uuid4
# Create your models here.

class Profile(models.Model):
    # user information
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    user_name = models.CharField(max_length=200, unique=True)
    short_intro = models.TextField(max_length=500, default='Hi there')
    about_me = models.TextField(max_length=500, default='네카라쿠배',null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    coding_start_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    # study group information
    solved_count = models.IntegerField(default=0, null=True, blank=True)
    group_id = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True, blank=True)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner)

class Algorithm(models.Model):
    language_choices = [
        ('Python3', 'Python3'),
        ('PyPy3', 'PyPy3'),
        ('Java11', 'Java11'),
        ('C99', 'C99'),
        ('C++17', 'C++17'),
        ('JS', 'JS'),
        ('GO', 'GO'),
        ('Ruby', 'Ruby'),
    ]
    type_choices = [
        ('Implementation', 'Implementation'),
        ('Greedy', 'Greedy'),
        ('String', 'String'),
        ('DataStructures', 'DataStructures'),
        ('Graphs', 'Graphs'),
        ('DP', 'DP'),
        ('Math', 'Math'),
        ('Bruteforce', 'Bruteforce'),
        ('etc', 'etc')
    ]
    profile_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.CharField(max_length=10, choices=language_choices)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    link = models.URLField(max_length=200)
    type = models.CharField(max_length=20, choices=type_choices)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=500, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    is_invite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name + self.subject

    class Meta:
        ordering = ['is_read', '-created']