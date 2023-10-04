from django.db import models


class Account_type(models.Model):
    name = models.CharField(max_length = 10)
    description = models.TextField(max_length = 10)


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
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    acc_type = models.ForeignKey(Account_type, on_delete=models.CASCADE)
    account_balance = models.IntegerField()
    status = models.CharField(max_length= 10, choices= ACCOUNT_OPTIONS)
     




