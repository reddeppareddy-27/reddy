from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return self.name

class Gym(models.Model):
    image = models.ImageField(upload_to='gym_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="gyms")
    google_maps_link = models.URLField()

    def __str__(self):
        return self.name
