from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name