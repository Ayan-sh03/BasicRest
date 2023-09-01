from django.db import models

# Create your models here.
class Url(models.Model):
    short_url = models.CharField(max_length=10)
    long_url = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.short_url
    
class Todo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return self.title