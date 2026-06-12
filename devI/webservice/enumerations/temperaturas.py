from django.db import models
class Temperatura(models.TextChoices):
    Fahrenheit = 'F','fahrenheit'
    Celcius = 'C','celcius'
    Kelvin = 'K','kelvin'
