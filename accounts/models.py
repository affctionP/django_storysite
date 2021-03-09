
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
class User(AbstractUser):
    class Meta:
        db_table='fun_user'
    avatar=models.ImageField(upload_to="profiles_pic",blank=True,verbose_name='آواتار')
    bio=models.CharField(max_length=600 ,blank=True,verbose_name='بیوگرافی')
    is_writer=models.BooleanField(default=False,verbose_name='نویسنده')



# Create your models here.
