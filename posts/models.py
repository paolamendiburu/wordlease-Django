from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    full_text = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    publication_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
