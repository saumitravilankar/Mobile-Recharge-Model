from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=14,null=False,blank=False,unique=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def getuserdebitcards(self):
        cards = self.debitcard_set.all()
        return cards

    def __str__(self) -> str:
        return self.username

class Wallet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=50)
    timestamp = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return self.user.username

class DebitCard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=12,unique=True)
    balance = models.PositiveIntegerField(default=10000)
    expiration_date = models.CharField(max_length=6)
    cvv = models.CharField(max_length=3)
    card_owner = models.CharField(max_length=500,null=True)
    card_added = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return self.user.username + str(self.card_number)