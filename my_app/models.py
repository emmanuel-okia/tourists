from django.db import models

class Warden(models.Model):
    WARDEN_CHOICES =[
        ("M","male"),
        ("F","female"),
    ]
    warden_name = models.CharField(max_length=50)
    warden_address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=30,null=True, blank=True)
    warden_photo = models.ImageField(upload_to="images/",default=True)
    def __str__(self): 
        return f"{self.warden_name}"



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
    def __str__(self): 
        return f"{self.name}"



class Wild(models.Model):
    species_type = models.CharField(max_length=50)
    no_of_species = models.IntegerField()
    game_park = models.ForeignKey(Game_park, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.species_type}"

    


class Visitor (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=40, null=True,blank=True)
    address = models.CharField(max_length=40,null=True, blank=True)
    wild_life = models.ForeignKey(Wild, on_delete=models.CASCADE)
    def __str__(self): 
        return f"{self.name}"
    


class Payment(models.Model):
    PAYMENT_CHOICES =[
        ("p","paid"),
        ("np","not paid"),
    ]
    pay_date = models.DateField(auto_now=False, auto_now_add=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    amount = models.IntegerField()
    received_by = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self): 
        return f"{self.pay_date}"
    
    


    




    
    