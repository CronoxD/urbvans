
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
        'status': 'ACTIVE',
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
            'status': 'ACTIVE',
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
        van_num_1 = sample_van(economic_number='NUM', plates='NUM-001')
        self.assertEqual(van_num_1.economic_number, 'NUM-0001')

        van_tar_1 = sample_van(economic_number='TAR', plates='TAR-001')
        self.assertEqual(van_tar_1.economic_number, 'TAR-0001')

        van_num_2 = sample_van(economic_number='NUM', plates='NUM-002')
        self.assertEqual(van_num_2.economic_number, 'NUM-0002')

        van_num_3 = sample_van(economic_number='NUM', plates='NUM-003')
        self.assertEqual(van_num_3.economic_number, 'NUM-0003')

    def test_economic_number_dont_repeat(self):
        """Test the economic number dont repeat when is deleted"""

        sample_van(economic_number='TAR', plates='TAR-001') # SN: TAR-0001

        van_tar_2 = sample_van(economic_number='TAR', plates='TAR-002') # SN: TAR-0002
        van_tar_2.delete()

        van_num_1 = sample_van(economic_number='NUM', plates='TAR-002') #  # SN: NUM-0001
        self.assertEqual(van_num_1.economic_number, 'NUM-0001')

        van_tar_3 = sample_van(economic_number='TAR', plates='TAR-003') # SN: TAR-0003
        self.assertEqual(van_tar_3.economic_number, 'TAR-0003')

    def test_similar_economic_number(self):
        """Test secuence economic number with similar initials"""
        sample_van(economic_number='TAR', plates='TAR-001') # SN: TAR-0001

        van_tara_1 = sample_van(economic_number='TARA', plates='TAA-001') # SN: TARA-0001
        self.assertEqual(van_tara_1.economic_number, 'TARA-0001')

        van_tar_2 = sample_van(economic_number='TAR', plates='TAR-002') # SN: TAR-0001
        self.assertEqual(van_tar_2.economic_number, 'TAR-0002')
