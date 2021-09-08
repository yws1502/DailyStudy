from django.db.models.signals import post_save


from django.contrib.auth.models import User
from .models import *


def create_profile(sender, instance, created, **kwargs):
    # 회원가입을 하면 자동으로 profile의 일부를 채워주기
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

post_save.connect(create_profile, sender=User)