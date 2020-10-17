from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, username, password):
        """
        Create and save a User with the given email, username and password.
        """
        if not email:
            raise ValueError(('User must have an email.'))
        if not username:
            raise ValueError(('User must have a username.'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        email = self.normalize_email(email)
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active =True
        user.save()

        

       


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email             = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username          = models.CharField(max_length=200)
    date_joined       = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login        = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin          = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    is_staff          = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email


     






