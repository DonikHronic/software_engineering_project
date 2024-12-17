from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from online_delivery.manager import CustomUserManager


# Create your models here.
class BaseUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD: str = "username"
    REQUIRED_FIELDS: list[str] = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username


class Client(BaseUser):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class RestaurantAdmin(BaseUser):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.id})


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.id})

    class Meta:
        ordering = ['-id']


class Order(models.Model):
    """Orders model"""

    class StatusChoices(models.TextChoices):
        NEW = "NEW"
        STARTED = "STARTED"
        ON_DELIVERY = "ON_DELIVERY"
        DELIVERED = "DELIVERED"

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_count = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    status = models.CharField(
        choices=StatusChoices, max_length=50, default=StatusChoices.NEW
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("order-detail", kwargs={"pk": self.id})

    class Meta:
        ordering = ['-id']
