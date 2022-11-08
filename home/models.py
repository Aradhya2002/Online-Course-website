from django.db import models
from .validators import file_size

# Create your models here.
class saveregister(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=50)
    password=models.CharField(max_length=50, default="")

class video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y", validators=[file_size])
    def __str__(self):
        return self.caption + ":" + str(self.video)

class teacher(models.Model):
    tname=models.CharField(max_length=50)
    temail=models.EmailField(max_length=50)
    tnumber=models.CharField(max_length=50)
    tpassword=models.CharField(max_length=50, default="")