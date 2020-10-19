from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): 
        self.name = (self.name).capitalize() 
        super(Author, self).save(*args, **kwargs) 


class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    body = RichTextField()
    
    def __str__(self):
        return self.title