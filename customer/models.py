from django.db import models

class Customer(models.Model):
  name = models.CharField("Name", max_length=200)
  email = models.EmailField()
  created = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.name