
# Django
from django.test import TestCase
from django.db.utils import IntegrityError

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
        self.assertEqual(van.economic_number, f'{data["economic_number"]}-0001')
        self.assertEqual(van.seats, data['seats'])
        self.assertEqual(van.status, data['status'])
        self.assertEqual(van.created_at.date(), datetime.date.today())

    def test_plates_are_unique(self):
        """Test plates are unique"""
        with self.assertRaises(IntegrityError):
            sample_van()
            sample_van()

    def test_economic_number_secuence(self):
        """Test the economic number secuence generation"""
        van1 = sample_van(economic_number='NUM', plates='TAX-001')
        self.assertEqual(van1.economic_number, 'NUM-0001')

        van2 = sample_van(economic_number='NUM', plates='TAX-002')
        self.assertEqual(van2.economic_number, 'NUM-0002')

        van3 = sample_van(economic_number='NUM', plates='TAX-003')
        self.assertEqual(van3.economic_number, 'NUM-0003')
