from django.db import models
from django.utils import timezone
from wallet.models import User

# Create your models here.
class Plan(models.Model):
    topup_amount = models.PositiveIntegerField()
    talktime = models.PositiveIntegerField()
    validity_in_days = models.IntegerField(default=30)

    def __str__(self) -> str:
        return 'plan' + ' of ' +str(self.topup_amount)

    class Meta:
        ordering = ['topup_amount']

class Main( ):
    TYPES = (
        ('PREPAID', 'PREPAID'),
        ('POSTPAID', 'POSTPAID')
    )
    OPERATORS = (
        ('RELIANCE', 'RELIANCE'),
        ('TATA DOCOMO', 'TATA DOCOMO'),
        ('VODAFONE', 'VODAFONE'),
        ('IDEA', 'IDEA'),
        ('MTNL', 'MTNL'),
        ('AIRCEL', 'AIRCEL'),
        ('AIRTEL', 'AIRTEL'),
        ('MTS', 'MTS')
    )
    CIRCLES = (
        ('MAHARASHTRA & GOA', 'MAHARASHTRA & GOA'),
        ('DELHI', 'DELHI'),
        ('GUJARAT', 'GUJARAT'),
        ('HARYANA', 'HARYANA'),
        ('KOLKATA', 'KOLKATA'),
        ('PUNJAB', 'PUNJAB'),
        ('RAJASTHAN', 'RAJASTHAN'),
        ('TAMILNADU', 'TAMILNADU'),
        ('KERALA', 'KERALA'),
        ('JAMMU AND KASHMIR', 'JAMMU AND KASHMIR')
    )

class Recharge(models.Model):

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    phone_number = models.CharField(max_length=14,null=False,blank=False)
    type = models.CharField(choices=Main.TYPES,max_length=10)
    operator = models.CharField(choices=Main.OPERATORS,max_length=15)
    circle = models.CharField(choices=Main.CIRCLES,max_length=20)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.phone_number) +' :'+' plan '+ str(self.plan.topup_amount)