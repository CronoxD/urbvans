
# Django
from django.test import TestCase

# Models
from vans.models import Van


class ModelTests(TestCase):

    def test_create_a_van_successful(self):
        """Test creating a new van is successful"""
        plates = 'AW3-123'
        economic_number = 'A1-0001'
        seats = 6
        status = 'Activa'

        van = Van.objects.create(
            plates=plates,
            economic_number=economic_number,
            seats=seats,
            status=status
        )

        self.assertEqual(van.plates, plates)
        self.assertEqual(van.economic_number, economic_number)
        self.assertEqual(van.seats, seats)
        self.assertEqual(van.status, status)
