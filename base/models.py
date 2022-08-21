from django.db import models

# Create your models here.

class Item(models.Model):
  item = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-updated','-created']

  def __str__(self) -> str:
    return self.item
  