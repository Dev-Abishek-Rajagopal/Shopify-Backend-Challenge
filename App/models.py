from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

import datetime
# Create your models here.



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, firstname, lastname, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_("Kindly assign is_staff=True for SuperUser"))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_("Kindly assign is_superuser=True for SuperUser"))

        return self.create_user(email, username, firstname, lastname, password, **other_fields)

    def create_user(self, email, username, firstname, lastname, password, **other_fields):

        if not email:
            raise ValueError(_("Kindly enter a valid Email Address"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,firstname=firstname,lastname=lastname,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class RepUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(_("Email Address"), unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150, blank=False)
    lastname = models.CharField(max_length=150, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = CustomAccountManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username","firstname","lastname"]

    def __str__(self):
        return self.username

SCOPE_CHOICES = (
    ("PUBLIC", "public"),
    ("PRIVATE", "PRIVATE"),
)

ACCESS_CHOICES = (
    ("READONLY", "readonly"),
    ("FULLACCESS", "FULL"),
)

def upload_to(instance,filename):
    return 'ImgRep/{filename}'.format(filename=filename)

def default_to():
    return "Image_"+ str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))

def default_rep():
    return "ImgRep/default_"+ str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))+".jpg"

class ImgRep(models.Model):

    img = models.ImageField(_("Image File"), upload_to=upload_to, default=default_rep)
    name = models.CharField(max_length=150, default=default_to)
    user = models.ForeignKey(RepUser, on_delete=models.CASCADE,related_name='Rep_User')
    scope = models.CharField(
        max_length = 20,
        choices = SCOPE_CHOICES,
        default = "PUBLIC"
        )
    access = models.CharField(
        max_length=20,
        choices=ACCESS_CHOICES,
        default="READONLY"
    )
    price = models.DecimalField(max_digits=10,decimal_places = 2,default=2.00)
    discount = models.IntegerField(default=10)
    color_palette = models.CharField(max_length=150, default="")

class ImgCart(models.Model):

    user = models.ForeignKey(RepUser, on_delete=models.CASCADE, related_name='Cart_User')
    img = models.ForeignKey(ImgRep, on_delete=models.CASCADE, related_name='Cart_Img')
    quantity = models.IntegerField(default=1)


