from django.db import models

# Create your models here.
class Post(models.Model):
  header = models.CharField(max_length=255)
  description = models.TextField()
  user = models.IntegerField(null=True, blank=True)
