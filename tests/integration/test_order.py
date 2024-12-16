from django.test import TestCase, Client
from django.urls import reverse

from online_delivery.models import BaseUser, Product, ProductCategory, Restaurant, Order


class OrderIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = BaseUser.objects.create_user(
            username="testuser", password="password", email="test@email.com"
        )
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
        self.client.login(username="testuser", password="password")

    def tearDown(self):
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()
        Restaurant.objects.all().delete()
        BaseUser.objects.all().delete()

    def test_create_order(self):
        response = self.client.post(
            reverse("create-order"), {"product_id": self.product.id, "count": 2}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.product, self.product)
        self.assertEqual(order.product_count, 2)

    def test_order_list_view(self):
        Order.objects.create(
            product=self.product, user=self.user, price=100, product_count=2
        )
        response = self.client.get(reverse("orders"))
        self.assertEqual(response.status_code, 200)

    def test_order_detail_view(self):
        order = Order.objects.create(
            product=self.product, user=self.user, price=100, product_count=2
        )
        response = self.client.get(reverse("order-detail", kwargs={"pk": order.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
