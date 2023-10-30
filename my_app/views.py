from django.shortcuts import render
from my_app.forms import WardenForm
from my_app.forms import Game_parkForm
from my_app.forms import WildForm
from my_app.forms import VisitorForm
from my_app.forms import PaymentForm





def index_view(request):
    return render(request, 'index.html')

def wild_view(request):
    return render(request, 'wild.html')

def warden_view(request):
    return render(request, 'warden.html')

def game_park_view(request):
    return render(request, 'game_park.html')



def add_warden_view(request):
    if request.method == "POST":
        warden_form = WardenForm(request.POST)

        if warden_form.is_valid():
            warden_form.save()

    else:
        warden_form = WardenForm()


    context ={
        'form':warden_form,
    }
    return render(request, "add_warden.html", context)

def add_game_park_view(request):
    if request.method == "POST":
        game_park_form = Game_parkForm(request.POST)

        if game_park_form.is_valid():
            game_park_form.save()

    else:
        game_park_form = Game_parkForm()


    context ={
        'form':game_park_form,
    }
    return render(request, 'add_game_park.html', context)

def add_wild_view(request):
    if request.method =="POST":
        wild_form = WildForm(request.POST)

        if wild_form.is_valid():
            wild_form.save()

    else:
        wild_form = WildForm()

    context ={
        'form':wild_form,
    }

    return render(request, "add_wild.html", context)

def add_visitor_view(request):
    if request.method =="POST":
        visitor_form = VisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor_form.save()

    else:
        visitor_form = VisitorForm()

    context ={
        'form':visitor_form,
    }

    return render(request, "add_visitor.html", context)


def add_payment_view(request):
    if request.method =="POST":
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()

    else:
        payment_form = PaymentForm()

    context ={
        'form':payment_form,
    }

    return render(request, "add_payment.html", context)



