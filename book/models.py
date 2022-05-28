from django.db import models
from core.models import User

# Create your models here.
class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return f"{self.title} | {self.author} | {self.owner.email}"