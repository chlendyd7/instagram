from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import resolve_url
# 장고 정규표현식

# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'
    
    # 팔로워 
    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True,
                              choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일을 업로드 해주세요")
    @property #이게뭐고?
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)
 

# class Profile(models.Model):
#     pass