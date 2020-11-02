from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class ATMachine(models.Model): 
    STATUS_CHOICES = (
        ("active", "Active"),
        ("deactivated", "Deactivated")
    )

    atm_machine_uid = models.BigIntegerField(
        primary_key = True, 
        validators = [MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    current_balance = models.BigIntegerField()
    location = models.CharField(
        max_length = 100
    )
    minimum_balance = models.BigIntegerField()
    status = models.CharField(
        max_length = 15,
        choices = STATUS_CHOICES
    )
    last_refill_date = models.DateField()
    next_maint_date = models.DateField()



class ATMachineRefill(models.Model): 
    refill_id = models.BigIntegerField(
        primary_key = True,
        validators = [MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    atm_machine_uid = models.ForeignKey(
        ATMachine, 
        on_delete = models.CASCADE,
        verbose_name = "ATM Machine UID"
    )
    amount = models.BigIntegerField()
    atm_branch = models.CharField(
        max_length = 30
    )
    refill_date = models.DateField()
    previous_balance = models.BigIntegerField()