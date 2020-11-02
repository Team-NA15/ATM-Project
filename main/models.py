from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.apps import apps
from administrator.models import ATMachine
from user.models import ATMCard
from django.utils import timezone


# Create your models here.
class Transaction(models.Model):
    STATUS_CHOICES = (
        ('canceled', 'Canceled'), 
        ('pending', 'Pending'), 
        ('complete', 'Complete')
    ) 
    transaction_id = models.AutoField(
        primary_key = True, 
        default = 1000000000
    )
    atm_card_number = models.ForeignKey(
        ATMCard, 
        to_field = 'card_number',
        on_delete = models.DO_NOTHING,
        verbose_name = 'atm card number'
    )
    date = models.DateField(
        default = timezone.now
    ) 
    atm_machine_uid = models.ForeignKey(
        ATMachine, 
        to_field = 'atm_machine_uid',
        on_delete = models.DO_NOTHING,
        verbose_name = 'atm machine uid'
    )
    status = models.CharField(
        max_length = 12, 
        choices = STATUS_CHOICES, 
        default = 'pending'
    )
    response_code = models.BigIntegerField(
        validators = [MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    transaction_type = models.CharField(
        max_length = 30
    )