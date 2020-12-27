
# Django
from django.test import TestCase

# Models
from vans.models import Van

# Utilities
import datetime


def sample_van(**params):
    """Create and return a sample van"""
    defaults = {
        'plates': 'AW3-123',
        'economic_number': 'A1-0001',
        'seats': 6,
        'status': 'Activa',
    }
    defaults.update(params)

    return Van.objects.create(**defaults)


class ModelTests(TestCase):

    def test_create_a_van_successful(self):
        """Test creating a new van is successful"""
        van = sample_van()

        self.assertEqual(van.plates, plates)
        self.assertEqual(van.economic_number, economic_number)
        self.assertEqual(van.seats, seats)
        self.assertEqual(van.status, status)
        self.assertEqual(van.created_at, datetime.date.today())

    def test_plates_format(self):
        """Test model van don't save when plates format is not correct"""
        with self.assertRaises(ValueError):
            sample_van(plates='A1-0001')

        with self.assertRaises(ValueError):
            sample_van(plates='AWS3-123')

    def test_status_vans(self):
        """Test models van only accept the status 'Activa' and 'En reparación'"""
        van = sample_van(status='Activa')
        self.assertIsNotNone(van.pk)

        van = sample_van(status='En reparación')
        self.assertIsNotNone(van.pk)

        with self.assertRaises(ValueError):
            sample_van(status='this_status_does_not_exists')
