 from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    neighborhood = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    scheduled_date = models.DateField()
    no_show = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date}"
