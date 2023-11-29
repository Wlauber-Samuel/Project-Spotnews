from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)

    def __str__(self):
        return self.name


def validate_title(title):
    words = title.split()
    if len(words) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class User(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", blank=True)
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.title
