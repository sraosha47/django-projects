from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_text = models.CharField("Description", max_length=200)
    funds = models.IntegerField("Initial Funds")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")

class Category(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category_text = models.CharField("Description", max_length=200)

class Entry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    entry_text = models.CharField("Description", max_length=200)
    costs = models.IntegerField()
