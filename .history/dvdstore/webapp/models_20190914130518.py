from django.db import models
from django.contrib.auth.models import User

#Here we will define our models, Like customer, employee etc. It will the be exported my django
#into postgres server


class Transaction(models.Model):
    users_ID= models.CharField(max_length=250)
    TransactionNumber = models.CharField(max_length=250)
    RentDate= models.CharField(max_length=250)
    DueDate = models.CharField(max_length=255) 
    MovieTitle = models.CharField(max_length=255)
    Payment_Method= models.CharField(max_length=255)
    Amount = models.CharField(max_length=250)
    dvdID=models.CharField(max_length=250)
    

class DVD(models.Model):
   # DVD_ID = models.IntegerField(max_length=10, default=1)
    Title= models.CharField(max_length=50)
    year = models.CharField(max_length=255) 
    genre = models.CharField(max_length=255)
    InStock= models.BooleanField(default=True)
    Synopsis= models.TextField()
    # Booking = models.IntegerField(default=1) 
    BookingPickup = models.CharField(max_length=255)
    NumOfTimesRented= models.IntegerField(default=0)
    ImageDVD= models.ImageField(upload_to='pics')
    PriceDVD = models.IntegerField(default=0)
    NumDaysBooked = models.IntegerField(default=0)
    # user_id= models.ForeignKey(User,on_delete=models.CASCADE)


class Fraud(models.Model):
    FraudID=models.IntegerField()
    FraudScore=models.IntegerField()
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)

class Customer(User.Model):
    phone_number= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    identification = models.CharField(max_length=13)
