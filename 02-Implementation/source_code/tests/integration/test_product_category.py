from django.test import TestCase, Client
from django.urls import reverse

from online_delivery.models import ProductCategory, Product, Restaurant


class ProductCategoryIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = ProductCategory.objects.create(
            name="Test Category",
            description="Test Description",
            image="300x300-Placeholder-Image.jpg",
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Desc",
            category=self.category,
            image="300x300-Placeholder-Image.jpg",
            restaurant=Restaurant.objects.create(
                name="Test Restaurant", address="123 Street"
            ),
        )

    def tearDown(self):
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

    def test_category_list_view(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")

    def test_category_detail_view(self):
        response = self.client.get(
            reverse("category-detail", kwargs={"pk": self.category.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")
        self.assertContains(response, "Test Product")
