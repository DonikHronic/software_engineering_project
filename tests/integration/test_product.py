from django.test import TestCase, Client
from django.urls import reverse
from online_delivery.models import Product, ProductCategory, Restaurant


class ProductIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Street"
        )
        self.category = ProductCategory.objects.create(
            name="Test Category",
            description="Test Description",
            image="300x300-Placeholder-Image.jpg",
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Desc",
            category=self.category,
            restaurant=self.restaurant,
            image="300x300-Placeholder-Image.jpg",
        )

    def tearDown(self):
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()
        Restaurant.objects.all().delete()

    def test_product_list_view(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_detail_view(self):
        response = self.client.get(
            reverse("product-detail", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
