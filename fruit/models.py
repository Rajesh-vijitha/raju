from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    places = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='Fruit')
    colour = models.CharField(max_length=20)

    def __str__(self):
        return self.name

