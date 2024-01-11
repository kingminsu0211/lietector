from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The username field must be set')
#
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    nickname = models.CharField(default='',max_length=20, unique=True,blank=False)
    number = models.CharField(default='',max_length=20, unique=True,blank=False)

    class Meta:
        db_table = 'user_customuser'  # MySQL 테이블 이름과 일치하도록 설정

    def __str__(self):
        return self.username  #username을 반환하도록 변경
