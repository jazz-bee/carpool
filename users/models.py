import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# MODELS


class User(AbstractUser):
    # custom User model that inherits attributes and methods from default django User model
    email = models.EmailField(
        _('email address'), unique=True,
        help_text=_("Only UCA accounts allowed"),
        validators=[
            validators.RegexValidator(re.compile(
                r'\w+@uca\.edu\.ar'), _('Enter a valid email.'), 'invalid')
            # ^[\w.@+-]+$
        ]
    )

    is_driver = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    # using default=empty instead of null as its not recommended for strings
    phone_number = models.CharField(max_length=12, blank=True, default='')
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    # TO DO: REQUIRED_FIELDS = ['username','date_of_birth','first_name','last_name','gender']
    REQUIRED_FIELDS = ['username']

    # use custom manager to create users
    objects = CustomUserManager()

    class Meta:
        # rename DB table
        db_table = 'user'

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email

# TO DO PERMISIONS
    # def has_perm(self,perm,obj=None):
    #     return self.is_admin

    # def has_module_perms(self,opp_Label):
    #     return True
