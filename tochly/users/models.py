from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """modify the default django user manager model to replace username with email."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    # Remove the email field from the REQUIRED_FIELDS settings 
    # as it's automatically included as USERNAME_FIELD.
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    STATUS_OPTIONS = [
        ('', ''),
        ('In a Meeting', 'meeting'),
        ('Commuting', 'commuting'),
        ('Working Remotely', 'romote'),
        ('Sick', 'sick'),
        ('In Leave', 'leave'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True, db_index=True)
    online = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='')
    timezone = models.CharField(max_length=50, blank=True, null=True)

    @property
    def email(self):
      return self.user.email

    @property
    def full_name(self):
        return f'{user.first_name} {user.last_name}'

    def __str__(self):
        return self.full_name