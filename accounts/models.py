from django.db import models
import uuid
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, Group)


# Create your models here.
class UserManager(BaseUserManager):
    # def create_user(self, email, username, password=None):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, first name, last name and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, username, password):
    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, first name, last name and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, default=None, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=60)
    username = models.CharField(verbose_name='Username', max_length=30, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(verbose_name='Active status', default=True,
                                    help_text='Designates whether this user should be treated as active. Unselect '
                                              'this instead of deleting accounts.')
    staff = models.BooleanField(verbose_name='Staff status', default=False,
                                help_text='Designates whether the user can log into this admin assets.')
    admin = models.BooleanField(verbose_name='Superuser status', default=False,
                                help_text='Designates that this user has all permissions without explicitly '
                                          'assigning them.')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.pk = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        # The user is identified by their email address
        return f'{self.first_name} {self.last_name}'

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_superuser(self):
        """Is the user a Superuser?"""
        return self.admin
