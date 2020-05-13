from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Yeonlip

from yeonlip.serializers import YeonlipSerializer


YEONLIPS_URL = reverse('yeonlip:yeonlip-list')


class PublicYeonlipsApiTests(TestCase):
    """Test the publicly available yeonlips API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(YEONLIPS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateYeonlipsApiTests(TestCase):
    """Test the private yeonlips API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

#    def test_get_yeonlip_list(self):
#        """Test listing yeonlip list"""
#        res = self.client.get(YEONLIPS_URL, {'full_addr': 'test'})
#        self.assertEqual(res.status_code, status.HTTP_200_OK)
