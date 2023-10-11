from django.db import models


# Create your models here.
class Truck(models.Model):
    truck_plates = models.CharField(max_length=17)

    def __str__(self):
        return self.truck_plates


class Driver(models.Model):
    full_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    start_date = models.CharField(max_length=50, blank=True)
    salary = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.full_name


class Task(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.CharField(max_length=15)
    truck = models.ForeignKey(Truck, on_delete=models.PROTECT, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.title}'
