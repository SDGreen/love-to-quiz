from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=400)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    quiz_file = models.FileField(upload_to="quizzes/")
