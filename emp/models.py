from django.db import models

class Truck(models.Model):
    truck_id = models.AutoField(primary_key=True)
    truck_day = models.CharField(max_length=50)
    truck_departure_time = models.CharField(max_length=50)
    truck_truck = models.CharField(max_length=50)
    truck_number = models.CharField(max_length=50)
    truck_origin = models.CharField(max_length=50)
    truck_destination = models.CharField(max_length=50)
    truck_operator = models.CharField(max_length=50)
    truck_coloader = models.CharField(max_length=50, null=True, blank=True)
    truck_coolie = models.CharField(max_length=50, null=True, blank=True)
    truck_adr = models.CharField(max_length=50, null=True, blank=True)
    truck_order_number = models.CharField(max_length=50, null=True, blank=True)
    truck_street = models.CharField(max_length=100)
    truck_street_number = models.CharField(max_length=100)
    truck_postal_code = models.CharField(max_length=10, null=True, blank=True)
    truck_city = models.CharField(max_length=50)
    truck_country = models.CharField(max_length=50)
    phone_country_code = models.CharField(max_length=4)
    phone_area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=4)

    def __str__(self):
        return self.truck_truck + " " + self.truck_number
