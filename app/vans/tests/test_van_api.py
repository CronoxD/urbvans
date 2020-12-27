
# Django
from django.test import TestCase
from django.urls import reverse

# Django REST Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from vans.models import Van

# Serializers
from vans.serializers import VanSerializer


VANS_URL = reverse('vans:van-list')


def detail_url(van_uuid):
    return reverse('vans:van-detail', args=[van_uuid])


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


class VansApiCreateListTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_vans(self):
        """Test retrieving a list of vans"""
        sample_van()
        sample_van(plates='AWD-332')

        res = self.client.get(VANS_URL)

        vans = Van.objects.all()
        serializer = VanSerializer(vans, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_van_detail(self):
        """Test retrieve a van detail by uuid"""
        van = sample_van(plates='SSB-321')
        serializer = VanSerializer(van)

        url = detail_url(van.uuid)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_van(self):
        """Test update a van"""
        payload = {
            'plates': 'TTT-432',
            'status': 'REPAIR',
            'seats': 0
        }
        van = sample_van(plates='VMS-231')

        url = detail_url(van.uuid)
        res = self.client.patch(url, payload)

        van = Van.objects.get(uuid=van.uuid)
        serializer = VanSerializer(van)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_delete_van(self):
        """Test delete a van by uuid"""
        van = sample_van()

        url = detail_url(van.uuid)

        res = self.client.delete(url)

        exists = Van.objects.filter(uuid=van.uuid).exists()

        self.assertFalse(exists)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_formats_plates(self):
        """Test dont save if the format plates is not correct"""
        payload = {
            'plates': 'FMS1-231',
            'economic_number': 'A1',
            'seats': 6,
            'status': 'REPAIR',
        }

        res = self.client.post(VANS_URL, payload)
        exists = Van.objects.filter(plates=payload['plates']).exists()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(exists)

        payload['plates'] = 'FNS-32m'

        res = self.client.post(VANS_URL, payload)
        exists = Van.objects.filter(plates=payload['plates']).exists()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(exists)

    def test_status_values(self):
        """Test post only accept ACTIVE and REPAIR status"""

        payload = {
            'plates': 'FMS1-231',
            'economic_number': 'A1',
            'seats': 6,
            'status': 'NO_STATUS',
        }

        res = self.client.post(VANS_URL, payload)
        exists = Van.objects.filter(status=payload['status']).exists()

        self.assertFalse(exists)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unique_plates(self):
        """Test unique plates in vans"""
        van = sample_van()

        payload = {
            'plates': van.plates,
            'economic_number': 'A1',
            'seats': 6,
            'status': 'ACTIVE',
        }

        res = self.client.post(VANS_URL, payload)

        count_vans = Van.objects.filter(plates=payload['plates']).count()

        self.assertEqual(count_vans, 1)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_vans_by_status(self):
        """Test filter vans by status"""
        sample_van(status='Activo', plates='SSN-321')
        sample_van(status='En reparación', plates='TNS-321')
        sample_van(status='Activo', plates='OHT-321')

        vans = Van.objects.filter(status='ACTIVE')
        serializer = VanSerializer(vans, many=True)

        url = f'{VANS_URL}?status=ACTIVE'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_van(self):
        """Test creating van"""
        payload = {
            'plates': 'AW3-123',
            'economic_number': 'A1',
            'seats': 6,
            'status': 'REPAIR',
        }

        res = self.client.post(VANS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        van = Van.objects.get(uuid=res.data['uuid'])

        self.assertEqual(payload['plates'], van.plates)
        self.assertEqual(f'{payload["economic_number"]}-0001', van.economic_number)
        self.assertEqual(payload['seats'], van.seats)
        self.assertEqual(payload['status'], van.status)
