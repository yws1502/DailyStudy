from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # 회원가입을 하면 자동으로 profile의 일부를 채워주기
    if created == True:
        user = instance
        profile = Profile.objects.create(
            owner = user,
            user_name = user.username,
            email = user.email,
            name = user.first_name,
        )

@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    # 프로필 정보가 바뀌면 유저 정보도 갱신
    profile = instance
    user = profile.owner
    if created == False:
        user.firstname = profile.name
        user.username = profile.user_name
        user.email = profile.email
        user.save()

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    # 프로필이 삭제(회원탈퇴)가 되면 유저 정보도 지우기
    try:
        user = instance.owner
        user.delete()
    except:
        pass

# post_save.connect(create_profile, sender=User)
# post_save.connect(update_user, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)