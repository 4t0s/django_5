from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator


class Song(models.Model):
    class Genre(models.TextChoices):
        ROCK = ('rock')
        RAP = ('rap')
        HIPHOP = ('hiphop')
        CLASSICAL = ('classical')
        POP = ('pop')
        BLUZE = ('bluze')
        
    name = models.CharField(max_length = 255, validators = [RegexValidator(regex = r"^[A-Z]\w*$",)])
    author = models.CharField(max_length = 255, validators = [MinLengthValidator(10), MaxLengthValidator(255)])
    label = models.CharField(max_length = 255, validators = [MinLengthValidator(10), MaxLengthValidator(255)])
    producer = models.CharField(max_length = 255, validators = [MinLengthValidator(10), MaxLengthValidator(255)])
    genre = models.CharField(max_length = 255, choices=Genre.choices)
    year = models.IntegerField(validators = [MinValueValidator(1995), MaxValueValidator(2025)])
    def __str__(self):
        return f'{self.name}'