from django.test import TestCase
from online_delivery.models import Restaurant, RestaurantAdmin, BaseUser


class RestaurantIntegrationTests(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Street"
        )
        self.restaurant_admin = RestaurantAdmin.objects.create(
            username="test_adminuser", password="password", restaurant=self.restaurant
        )

    def tearDown(self):
        RestaurantAdmin.objects.all().delete()
        Restaurant.objects.all().delete()

    def test_restaurant_creation(self):
        self.assertEqual(Restaurant.objects.count(), 4)
        self.assertEqual(Restaurant.objects.last().name, "Test Restaurant")

    def test_restaurant_admin_creation(self):
        self.assertEqual(RestaurantAdmin.objects.count(), 1)
        self.assertEqual(RestaurantAdmin.objects.first().restaurant, self.restaurant)
