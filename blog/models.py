from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    text = models.CharField(max_length=480)
class article (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField( upload_to = 'blog_images/' ,default = 'default.png/' )
    author = models.ForeignKey(User , on_delete=models.CASCADE,default=None)
    #add in author later
    def __str__ (self):
        return self.title
    def snipped (self):
        if len(self.body)>50:
            return self.body[:50]+'...'
        else:
            return self.body
        