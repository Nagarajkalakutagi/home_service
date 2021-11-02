from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_staff(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), primary_key=True, unique=True)
    mobile = models.BigIntegerField(unique=True)
    is_user = models.BooleanField(default=True)
    address = models.CharField(max_length=200, blank=False)
    landmark = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()


class City(models.Model):
    city_name = models.CharField(max_length=25, db_index=True, unique=True)
    pin_code = models.PositiveIntegerField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('city_name',)

    def __str__(self):
        return self.city_name


class Service(models.Model):
    multiple_city = models.ManyToManyField(City)
    service_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('service_name',)

    def __str__(self):
        return self.service_name


class ServiceType(models.Model):
    service_name = models.ForeignKey(Service, related_name='service_type', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('service_type',)

    def __str__(self):
        return self.service_type


class ServiceCharge(models.Model):
    service_charge_name = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="images", blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.issue_type


class ServiceProvider(models.Model):
    staff_id = models.ForeignKey(MyUser, max_length=100, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, max_length=100, on_delete=models.CASCADE)


class BookAppointment(models.Model):
    user_id = models.ForeignKey(MyUser, max_length=100, on_delete=models.CASCADE)
    service_charge = models.ForeignKey(ServiceCharge, max_length=100, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    user_id = models.ForeignKey(MyUser, max_length=100, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    service_type = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CallbackRequest(models.Model):
    name = models.CharField(max_length=256)
    mobile = models.IntegerField(blank=True)
    body = models.TextField(blank=True)
    callback_timing = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name