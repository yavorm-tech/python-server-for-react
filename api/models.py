from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Credentials(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=32, default="")
    password = models.CharField(max_length=32, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username','url'], name='unique_fields')
        ]
    def number_of_ratings(self):
        ratings = Ratings.objects.filter(credential=self)
        return len(ratings);
    def avg_rating(self):
        sum = 0;
        ratings = Ratings.objects.filter(credential=self)
        for rating in ratings:
            sum += rating.stars
        if (len(ratings) > 0 ):
            return sum / len(ratings);
        else:
            return 0;
class Ratings(models.Model):
    credential = models.ForeignKey(Credentials, on_delete=models.CASCADE);
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','credential'], name='unique_fields_ratings')
        ]