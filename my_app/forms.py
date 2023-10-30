from django.forms import ModelForm
from my_app.models import Warden, Game_park, Wild, Visitor, Payment

class WardenForm(ModelForm):
    class Meta:
        model = Warden
        fields = '__all__'

class Game_parkForm(ModelForm):
    class Meta:
        model = Game_park
        fields = '__all__'

class WildForm(ModelForm):
    class Meta:
        model = Wild
        fields = '__all__'

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'



