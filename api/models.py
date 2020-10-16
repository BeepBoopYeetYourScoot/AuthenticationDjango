from django.db import models


class Farm(models.Model):

    class ShelterLocation(models.TextChoices):
        uptown = 'Uptown'
        downtown = 'Downtown'
        center = 'Center'
        industrial = 'Industrial'

    name = models.CharField(max_length=30)
    location = models.CharField(choices=ShelterLocation.choices, max_length=15, default="My uncles' basement")
    capacity = models.PositiveIntegerField()
    buy_price = models.PositiveIntegerField()
    farm_owner = models.ForeignKey('api.HomeOwner', related_name='owned_shelters', on_delete=models.CASCADE,
                                   null=True, default=None)

    def __str__(self):
        return self.name


class CatModel(models.Model):

    class CatSex(models.TextChoices):
        male = 'Male'
        female = 'Female'

    class CatColour(models.TextChoices):
        white = 'White'
        redhead = 'Redhead'
        black = 'Black'
        brown = 'Brown'

    sex = models.CharField(max_length=10, choices=CatSex.choices, default='Hermaphrodites')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    colour = models.CharField(choices=CatColour.choices, default='Ethereal', max_length=10)
    farm = models.ForeignKey('api.Farm', related_name='owned_cats', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name


class HomeOwner(models.Model):

    class Gender(models.TextChoices):
        male = 'Male'
        female = 'Female'

    class Occupation(models.TextChoices):
        entrepreneur = 'Entrepreneur'
        software_developer = 'Software Developer'
        engineer = 'Engineer'
        nail_master = 'Nail Master'
        vlogger = 'Vlogger'
        vtuber = 'Vtuber'

    gender = models.CharField(choices=Gender.choices, default='The owner has passed away', max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(choices=Occupation.choices, default='The owner has too much money', max_length=20)
    name = models.CharField(max_length=20, default='GivesMeConniptions')

    def __str__(self):
        return self.name
