
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
        'economic_number': 'A1',
        'seats': 6,
        'status': 'Activa',
    }
    defaults.update(params)

    return Van.objects.create(**defaults)


class ModelTests(TestCase):

    def test_create_a_van_successful(self):
        """Test creating a new van is successful"""
        data = {
            'plates': 'AW3-123',
            'economic_number': 'A1',
            'seats': 6,
            'status': 'Activa',
        }
        van = sample_van(**data)

        self.assertEqual(van.plates, data['plates'])
        self.assertEqual(van.economic_number, f'{data["economic_number"]}0001')
        self.assertEqual(van.seats, data['seats'])
        self.assertEqual(van.status, data['status'])
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

    def test_plates_are_unique(self):
        """Test plates are unique"""
        with self.assertRaises(ValueError):
            sample_van()
            sample_van()

    def test_economic_number_secuence(self):
        """Test the economic number secuence generation"""
        van1 = sample_van(economic_number='NUM')
        self.assertEqual(van1.economic_number, 'NUM-0001')

        van2 = sample_van(economic_number='NUM')
        self.assertEqual(van2.economic_number, 'NUM-0002')

        van3 = sample_van(economic_number='NUM')
        self.assertEqual(van3.economic_number, 'NUM-0003')
