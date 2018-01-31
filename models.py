from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firm = models.ForeignKey('firm.Firm', verbose_name='Firma', blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True, verbose_name='E-Mail')
    first_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Last Name')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='Address')
    image = models.ImageField(blank=True, null=True, verbose_name='Image')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Phone')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
