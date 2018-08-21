from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    full_text = models.TextField()
    image = models.FileField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)



def __str__(self):
    """
    Define cómo se representa un Ad como una string
    """
    return '{0}'.format(self.title)

