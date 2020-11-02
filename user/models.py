from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils import timezone


# Create your models here.

class AccountExtension(models.Model): 
    account_number = models.BigIntegerField(
        primary_key=True,
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    name = models.CharField(
        max_length = 35
    )
    phone_number = models.CharField(
        max_length = 10
    )
    balance = models.BigIntegerField()



class ATMCard(models.Model): 
    CARD_STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'deactivated')
    )
    card_number = models.BigIntegerField(
        primary_key=True,
        unique=True,
        validators=[MinValueValidator(1000000000000000),MaxValueValidator(9999999999999999)])
    account_number: models.ForeignKey(
        AccountExtension,
        on_delete=models.CASCADE, 
        verbose_name="account extension"
    )
    pin = models.IntegerField(
        validators=[MinValueValidator(1000),MaxValueValidator(9999)]
    )
    name = models.CharField(
        max_length=35
    )
    date_issued = models.DateField(),
    expire_date = models.DateField(), 
    address = models.CharField(
        max_length=70
    )
    two_fact_auth_status = models.BooleanField(),
    phone_number = models.CharField(
        max_length=10
    )
    card_status = models.CharField(
        max_length=15,
        choices=CARD_STATUS_CHOICES
    )

