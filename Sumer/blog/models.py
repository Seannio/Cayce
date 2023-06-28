from django.db import models

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

CATEGORY = (
   (0,"BLOGPOST"),
   (1,"ART"),
   (2,"MUSIC")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

