from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Yeonlip(models.Model):
    """Yeonlip Object"""
    full_addr = models.CharField(max_length=255)
    dong_addr = models.CharField(max_length=255)
    road_addr = models.CharField(max_length=255)
    bldg_nm = models.CharField(max_length=255)
    land_area = models.DecimalField(max_digits=19, decimal_places=2)
    base_area = models.DecimalField(max_digits=19, decimal_places=2)
    total_area = models.DecimalField(max_digits=19, decimal_places=2)
    struct_name = models.CharField(max_length=255)
    struct_others = models.CharField(max_length=255)
    main_use = models.CharField(max_length=255)
    other_use = models.CharField(max_length=255)
    roof_name = models.CharField(max_length=255)
    roof_others = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    above_floors = models.IntegerField()
    under_floors = models.IntegerField()
    passenger_elev = models.IntegerField()
    emergency_elev = models.IntegerField()
    land_price_m2 = models.IntegerField()
    area_usage = models.CharField(max_length=255)
    # location_point = models.JSONField()
    x = models.FloatField()
    y = models.FloatField()
    constr_date = models.CharField(max_length=255)
    est_price_m2 = models.IntegerField()
    est_price = models.IntegerField()

    def __str__(self):
        return self.full_addr

class Unit(models.Model):
    """Unit Object"""
    area = models.FloatField()
    block_name = models.CharField(max_length=255)
    floor_number = models.IntegerField()
    floor_type_code = models.IntegerField()
    floor_type_name = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    est_price_m2 = models.IntegerField()
    est_price = models.IntegerField()
    yeonlip_building = models.ForeignKey(Yeonlip, on_delete=models.CASCADE)

    def __str__(self):
        return self.block_name + ' ' + self.unit_name
