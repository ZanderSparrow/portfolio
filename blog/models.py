from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        