from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    def __str__(self):
        return self.title
class Posted(models.Model):
    title= models.CharField(max_length=300, unique=True)