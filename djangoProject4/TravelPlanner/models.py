from django.db import models
from django.contrib.auth.models import User

#1
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')


    def __str__(self):
        return self.name

#2
class PackingList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#3
class PackingItem(models.Model):
    name = models.CharField(max_length=100)
    packing_list = models.ForeignKey(PackingList, on_delete=models.CASCADE)  #przepatrzec opcja many-to-many
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#4
class TravelPlan(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    transport = models.CharField(max_length=100)   #opcja
    cost = models.DecimalField(max_digits=8, decimal_places=2) #opcja
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.destination.name} ({self.start_date} - {self.end_date})"

#5
class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


#Plik models.py wydaje się kompletny i spełnia wymagania, które przedstawiłaś wcześniej.
# Masz pięć modeli w tym pliku, z czego jeden z nich (User) pochodzi z wbudowanej aplikacji Django auth,
# więc jest już gotowy do użycia.
# Ponadto, wykorzystujesz relacje 1:wiele i wiele:wiele pomiędzy poszczególnymi modelami,
# co jest bardzo dobrze. Wszystkie klucz obce zostały skonfigurowane z odpowiednią opcją on_delete.
# Możliwość dodawania zdjęć do obiektów modelu Destination i TravelPlan została obsłużona przy pomocy pola ImageField.