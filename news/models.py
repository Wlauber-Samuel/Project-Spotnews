from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

# class News(models.Model):
#     title = models.CharField(max_length=200, unique=True, blank=False)
#     content = models.TextField(blank=False)
#     author = models.CharField(max_length=200, blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='img/', blank=True)
#     categories = models.ManyToManyField(Category, related_name='news')

#     def __str__(self):
#         return self.title
