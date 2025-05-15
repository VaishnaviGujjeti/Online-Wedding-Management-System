from django.test import TestCase
from .models import Service, Category  # Import both models

class ServiceTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        Service.objects.create(name="Test Service", price=100, category=self.category)

    def test_service_creation(self):
        service = Service.objects.get(name="Test Service")
        self.assertEqual(service.price, 100)
        self.assertEqual(service.category.name, "Test Category")
