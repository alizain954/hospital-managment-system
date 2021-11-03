from django.db import models

# Create your models here.4

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    special = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(null=True)
    gender = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name+'--'+self.patient.name
