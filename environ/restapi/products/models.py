from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): 
        self.name = (self.name).capitalize() 
        super(Author, self).save(*args, **kwargs) 
        

class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False, blank=False)
    body  = models.TextField(max_length=400, null=False, blank=False)
    
    def __str__(self):
        return self.title