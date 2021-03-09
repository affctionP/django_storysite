from django.db import models
from django.utils import timezone
from django.conf import settings
class PostModel(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,verbose_name='نویسنده')
    title=models.CharField(max_length=200,verbose_name='عنوان')
    text=models.TextField(verbose_name='متن')
    published_date = models.DateField(default=timezone.now,verbose_name='تاریخ انتشار')
    slug=models.SlugField(null=True,verbose_name='هشتگ')
    thumb=models.ImageField(upload_to='thumbnails/%Y/%m/%d',blank= True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comment')
    body=models.TextField(verbose_name='نظر')
    posted_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comm')
    created=models.DateField(default=timezone.now)

    class Meta:
        ordering=['created']


    def __str__(self):
         return 'commented {} by {} '.format(self.body,self.posted_by.username)





# Create your models here.
