from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class Profile(models.Model):
    # user information
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    user_name = models.CharField(max_length=200, unique=True)
    short_intro = models.TextField(max_length=500, default='Hi there🖐')
    about_me = models.TextField(max_length=500, default='네카라쿠배🛫',null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    # study group information
    solved_count = models.IntegerField(default=0, null=True, blank=True)
    group_id = models.CharField(max_length=200, null=True, blank=True)
    group_reader = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + '--' + self.user_name

# from django.db.models.signals import post_save

# def create_profile(sender, instance, created, **kwargs):
#     # 회원가입을 하면 자동으로 profile의 일부를 채워주기
#     print(created, '<<<<<<<<<<<<<<<<<<<')
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             owner = user,
#             user_name = user.username,
#             email = user.email,
#             name = user.first_name,
#         )

# post_save.connect(create_profile, sender=User)