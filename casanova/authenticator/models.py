from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class BasicUser(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)


class Provider(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Address(models.Model):
    number = models.CharField(max_length=10)
    street = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    def __str__(self):
        return "%s, %s, %s, %s"%(self.number, self.street, self.area, self.city)
        
class Venue(models.Model):
    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    DAYS = (
        (SUN, "Sunday"),
        (MON, "Monday"),
        (TUE, "Tuesday"),
        (WED, "Wednesday"),
        (THU, "Thursday"),
        (FRI, "Friday"),
        (SAT, "Saturday"),
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    capacity = models.IntegerField()
    price_per_hour = models.IntegerField()
    air_conditioned = models.BooleanField(default=False)
    catering_service = models.BooleanField(default=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    opening_day = models.CharField(max_length=3, choices=DAYS, default=SUN)
    closing_day = models.CharField(max_length=3, choices=DAYS, default=SAT)
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name

class Consumer(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.username
class Coupon(models.Model):
    code = models.CharField(max_length=10)
    discount = models.FloatField()
    count = models.IntegerField()

class Booking(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.PROTECT)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    amount = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()

class TimeSlot(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)


