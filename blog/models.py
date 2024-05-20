from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    # comments = 

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name="comments")