from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.urls import reverse

from restaurant_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    def __str__(self):
        return self.name
