from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

def sample_yeonlip():
    return models.Yeonlip.objects.create(
       full_addr = 'sample address',
       dong_addr = 'sample dong',
       road_addr = 'sample road',
       bldg_nm = 'sample name',
       land_area = 123.45,
       base_area = 123.45,
       total_area = 123.45,
       struct_name = 'sample name',
       struct_others = 'sample name',
       main_use =  'sample use',
       other_use = 'sample use',
       roof_name = 'sample name',
       roof_others = 'sample name',
       height = 123.45,
       above_floors = 12,
       under_floors = 1,
       passenger_elev = 1,
       emergency_elev = 1,
       land_price_m2 = 12345,
       area_usage = 'sample name',
       x = 123.45,
       y = 123.45,
       constr_date = 'int string', 
       est_price_m2 = 123456789,
       est_price = 12345678912345
    )


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@philthylove.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_yeonlip_str(self): 
        """Test the yeonlip string representation"""
        yeonlip = models.Yeonlip.objects.create(
            full_addr = 'sample address',
            dong_addr = 'sample dong',
            road_addr = 'sample road',
            bldg_nm = 'sample name',
            land_area = 123.45,
            base_area = 123.45,
            total_area = 123.45,
            struct_name = 'sample name',
            struct_others = 'sample name',
            main_use =  'sample use',
            other_use = 'sample use',
            roof_name = 'sample name',
            roof_others = 'sample name',
            height = 123.45,
            above_floors = 12,
            under_floors = 1,
            passenger_elev = 1,
            emergency_elev = 1,
            land_price_m2 = 12345,
            area_usage = 'sample name',
            # location_point = {'x': 123.45, 'y': 123.45},
            x = 123.45,
            y = 123.45,
            constr_date = 'int string',
            est_price_m2 = 123456789,
            est_price = 12345678912345
        )
        self.assertEqual(str(yeonlip), yeonlip.full_addr)

    def test_unit_str(self):
        """Test the unit string representation"""
        unit = models.Unit.objects.create(
            area = 123.45,
            block_name = 'A',
            floor_number = 1,
            floor_type_code = '20',
            floor_type_name = 'above',
            unit_name = '105',
            est_price_m2 = 1234,
            est_price = 1234567890,
            yeonlip_building = sample_yeonlip() 
        )
        self.assertEqual(str(unit), unit.block_name + ' ' + unit.unit_name)
