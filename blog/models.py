from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField()
    description = models.CharField(max_length = 500)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Blog(models.Model):
    
    
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    content = models.TextField(max_length=350)
    author = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, related_name = 'blog', on_delete = models.CASCADE)
    
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.author
    
