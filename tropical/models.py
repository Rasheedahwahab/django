from django.db import models



class Account_type(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField(max_length = 130)


class Branch(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    manager = models.CharField(max_length = 30)


class Account(models.Model):

    ACCOUNT_OPTIONS= [
        ("A", "active"),
        ("IN", "inactive"),
    ]

    account_number = models.CharField(max_length = 30)
    opening_date = models.DateField(auto_now = False)
    account_balance = models.IntegerField()
    status = models.CharField(max_length= 10, choices= ACCOUNT_OPTIONS)
    photo = models.ImageField(upload_to = "photos")

class Customer(models.Model):

    customer_name = models.CharField(max_length = 30)
    birth_dates = models.DateField(auto_now = False)
    address = models.CharField(max_length = 30)
    contact = models.CharField(max_length= 20)
    occupation = models.CharField(max_length = 30)

class Transaction(models.Model):


    MEDIUM_OPTIONS= [
    ("C", "cash"),
    ("CH", "cheque"),
    ("M", "money"),
]
    TYPE_OPTIONS= [
    ("D", "deposit"),
    ("W", "withdraw"),
]
    
    transaction_number = models.CharField(max_length = 30)
    transaction_date = models.DateField(auto_now = False)
    transaction_type = models.CharField(max_length= 10, choices= TYPE_OPTIONS)
    transaction_medium = models.CharField(max_length= 10, choices= MEDIUM_OPTIONS)
    





    

     




