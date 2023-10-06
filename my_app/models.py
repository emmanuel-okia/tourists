from django.db import models

class Warden(models.Model):
    GENDER_CHOICES =[
        ("M","male"),
        ("F","female"),
    ]
    warden_name = models.CharField(max_length=50)
    warden_address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=30,null=True, blank=True)



class Game_park (models.Model):
    LOCATION_CHOICES =[
        ("N", "NORTHERN"),
        ("W", "WESTERN"),
        ("S", "SOUTHERN"),
        ("E", "EASTERN"),
    ]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=40, null=True)
    contact_person = models.CharField(max_length=50)
    contact = models.CharField(max_length=40, null=True, blank=True)
    warden = models.ForeignKey(Warden,on_delete=models.CASCADE)



class Wild(models.Model):
    species_type = models.CharField(max_length=50)
    no_of_species = models.IntegerField()
    game_park = models.ForeignKey(Game_park, on_delete=models.CASCADE)


class Visitor (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=40, null=True,blank=True)
    address = models.CharField(max_length=40,null=True, blank=True)
    wild_life = models.ForeignKey(Wild, on_delete=models.CASCADE)


class Payment(models.Model):
    GENDER_CHOICES =[
        ("p","paid"),
        ("np","not paid"),
    ]
    pay_date = models.DateField(auto_now=False, auto_now_add=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    amount = models.IntegerField()
    received_by = models.CharField(max_length=40, null=True, blank=True)






    
    