from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from datetime import date, timedelta

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=200)
    sum_assurance = models.PositiveIntegerField()
    premium = models.PositiveIntegerField()
    tenure = models.PositiveIntegerField()
    creation_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')
    creation_date = models.DateField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.policy.policy_name

    def save(self, *args, **kwargs):
        if self.status == 'Approved' and self.start_date is None:
            self.start_date = date.today()
            self.end_date = self.start_date + timedelta(days=self.policy.tenure * 365)
        super().save(*args, **kwargs)

class Claim(models.Model):
    policy_record = models.ForeignKey(PolicyRecord, on_delete=models.CASCADE)
    reason = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=100, default='Pending')
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Claim for {self.policy_record.policy.policy_name}"

class PremiumPayment(models.Model):
    policy_record = models.ForeignKey(PolicyRecord, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.policy_record.policy.policy_name}"

class Question(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    admin_comment = models.CharField(max_length=200, default='Nothing')
    asked_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.description
