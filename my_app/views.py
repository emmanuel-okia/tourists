from django.shortcuts import render, redirect
from my_app.forms import WardenForm
from my_app.forms import Game_parkForm
from my_app.forms import WildForm
from my_app.forms import VisitorForm
from my_app.forms import PaymentForm

from my_app.models import Warden
from my_app.models import Game_park
from my_app.models import Wild
from my_app.models import Visitor
from my_app.models import Payment





def index_view(request):
    return render(request, 'index.html')

def wild_view(request):
    return render(request, 'wild.html')

def warden_view(request):
    return render(request, 'warden.html')

def game_park_view(request):
    return render(request, 'game_park.html')



def add_warden_view(request):
    message = ''
    if request.method == "POST":
        warden_form = WardenForm(request.POST)

        if warden_form.is_valid():
            warden_form.save()

            message = "addition successful"

    else:
        warden_form = WardenForm()
    
    warden = Warden.objects.all()


    context ={
        'form':warden_form,
        'msg':message,
        'warden': warden,
    }
    return render(request, "add_warden.html", context)

def add_game_park_view(request):
    message = ''
    if request.method == "POST":
        game_park_form = Game_parkForm(request.POST)

        if game_park_form.is_valid():
            game_park_form.save()
            message = "addition successful"

    else:
        game_park_form = Game_parkForm()
        game_park = Game_park.objects.all()


    context ={
        'form':game_park_form,
        'msg':message,
        'game_park': game_park,
    }
    return render(request, 'add_game_park.html', context)

def add_wild_view(request):
    message = ''
    if request.method =="POST":
        wild_form = WildForm(request.POST)

        if wild_form.is_valid():
            wild_form.save()
            message = "addition successful"

    else:
        wild_form = WildForm()
        wild = Wild.objects.all()

    context ={
        'form':wild_form,
        'msg':message,
        'wild': wild
    }

    return render(request, "add_wild.html", context)

def add_visitor_view(request):
    message = ''
    if request.method =="POST":
        visitor_form = VisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor_form.save()
            message = "addition successful"

    else:
        visitor_form = VisitorForm()
        visitor = Visitor.objects.all()

    context ={
        'form':visitor_form,
        'msg':message,
        'visitor': visitor
    }

    return render(request, "add_visitor.html", context)


def add_payment_view(request):
    message = ''
    if request.method =="POST":
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()

            message = "addition successful"

    else:
        payment_form = PaymentForm()
        payment = Payment.objects.all()

    context ={
        'form':payment_form,
        'msg':message,
        'payment': payment
    }

    return render(request, "add_payment.html", context)



def edit_warden_view(request, warden_id):
    message = ''
    warden = Warden.objects.get(id= warden_id)

    if request.method == "POST":
        warden_form = WardenForm(request.POST, instance=warden)

        if warden_form.is_valid():
            warden_form.save()
            message = "saved successfully"

        else:
            message = "saved data is ivalid"

    else:
        warden_form = WardenForm(instance=warden) 

    context = {
        'form':warden_form,
        'warden':warden,
        'message': message 
    }

    return render(request, "edit_warden.html", context)



def delete_warden_view(request, warden_id):
    warden = Warden.objects.get(id= warden_id)

    warden.delete()

    return redirect(add_warden_view)



