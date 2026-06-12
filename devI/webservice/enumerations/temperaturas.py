from django.db import models

class Temperatura(models.TextChoices):
    
    CELCIUS = "°C", "Celcius"
    FAHRENHEIT = "°F", "Fahrenheit"
    KELVIN = "°K", "Kelvin"
