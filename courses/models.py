from django.db import models
from django.utils.text import slugify


# Create your models here.

from blog.models import Category


class Course(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, related_name='course', on_delete = models.CASCADE)
    slug = models.SlugField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    