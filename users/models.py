from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


'''
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class AccountManager(BaseUserManager):
    #def create_user(self, email, date_of_birth, password=None):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #def create_superuser(self, email, date_of_birth, password):
    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            #date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #date_of_birth = models.DateField()
    username = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['date_of_birth']

    def get_username(self):
        return self.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
'''