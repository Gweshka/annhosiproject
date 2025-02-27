from django.db import models

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    date=models.DateField()
    message=models.TextField()
    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    Department = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.Status

class Staff(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=50)
    position=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    datehired=models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname

class Ward(models.Model):
    name=models.CharField(max_length=40)
    totalbeds=models.IntegerField()
    bedsavailable=models.IntegerField()
    def __str__(self):
        return self.name




