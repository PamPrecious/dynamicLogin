from django.db import models

# Create your models here.

class Dashboard(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    service = models.CharField(max_length=100)

    dashboard_view = ["name","contact","address","service"]

class Clients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    
    clients_view = ["name","email","contact","address","service"]

class User(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=100)
    contact = models.IntegerField()
    
    user_view = ["name","category","contact"]

class Tasks(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    contact = models.IntegerField()
    task = models.CharField(max_length=30)
    client =models.CharField(max_length=30)
    
    tasks_view = ["name","category","contact","task","client"]










