from django.contrib import admin
from .models import Warden, Game_park,Wild,Visitor,Payment

class WardenAdmin(admin.ModelAdmin):
    list_display = ("warden_name","warden_address","contact")

class Game_parkAdmin(admin.ModelAdmin):
    list_display = ("name","address","contact_person","contact","warden")


class WildAdmin(admin.ModelAdmin):
    list_display = ("species_type","no_of_species","game_park")


class VisitorAdmin(admin.ModelAdmin):
    list_display = ("name","age","contact","address","wild_life")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("pay_date","visitor","amount","received_by")



admin.site.register(Warden, WardenAdmin)
admin.site.register(Game_park, Game_parkAdmin)
admin.site.register(Wild, WildAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Payment, PaymentAdmin)