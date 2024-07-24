from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()   #Model
# Create your models here.
class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio =models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_iamges', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    # python manage.py createsuperuser
    # admin@socialbook.com
    # socialbook=pw
    
