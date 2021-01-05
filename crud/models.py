from django.db import models
from django.urls import reverse

# Create your models here.
class Crud_r(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')
