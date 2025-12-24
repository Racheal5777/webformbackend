from django.db import models

class UserDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    state= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
# Create your models here.
