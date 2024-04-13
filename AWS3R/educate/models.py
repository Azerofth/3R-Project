from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimestampModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tags(TimestampModel):
    tags_name = models.CharField(max_length = 180)
    tags_description = models.TextField(max_length = 250)

    def __str__(self):
        return self.tags_name

class Post(TimestampModel):
    post_title = models.CharField(max_length=180)
    post_description = models.TextField(max_length=250)
    post_image = models.FileField(upload_to='postimages/')
    post_tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

