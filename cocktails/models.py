from django.db import models
from django.contrib.auth.models import User

class FavoriteCocktail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cocktail_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name