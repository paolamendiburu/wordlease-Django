from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey(User, related_name="blog", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Define cómo se representa un Ad como una string
        """
        return '{0} | Owner: {1}'.format(self.name, self.owner)

class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
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



