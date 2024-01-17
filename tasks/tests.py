from django.test import TestCase
from django.contrib.gis.geos import Point
from .models import Shop

class ShopModelTest(TestCase):
    def setUp(self):
        # Create a sample Shop instance
        self.shop = Shop.objects.create(
            name='Test Shop',
            location=Point(1.0, 2.0),  # Example coordinates (longitude, latitude)
            address='123 Test Street'
        )

    def test_shop_creation(self):
        # Check if the Shop instance was created successfully
        self.assertEqual(self.shop.name, 'Test Shop')
        self.assertEqual(self.shop.location.x, 1.0)
        self.assertEqual(self.shop.location.y, 2.0)
        self.assertEqual(self.shop.address, '123 Test Street')

    def test_shop_str_method(self):
        # Check the __str__ method returns the expected string
        expected_str = 'Test Shop'
        self.assertEqual(str(self.shop), expected_str)

    def test_shop_query(self):
        # Query the database to check if the saved data matches
        queried_shop = Shop.objects.get(name='Test Shop')
        self.assertEqual(queried_shop.name, 'Test Shop')
        self.assertEqual(queried_shop.location, Point(1.0, 2.0))
        self.assertEqual(queried_shop.address, '123 Test Street')
