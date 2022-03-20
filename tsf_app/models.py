from django.db import models

# Create your models here.
class TransactionDetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    debit_amount = models.IntegerField()
    credit_amount = models.IntegerField()
    account_balance = models.IntegerField()

    def __str__(self):
        return self.name +' Account Balance: ' + str(self.account_balance)
    

class CustomerDetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    available_balance = models.IntegerField()

    def __str__(self):
        return self.name 