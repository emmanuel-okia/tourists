from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
from django.contrib import messages




@login_required
def index_view(request):
    return render(request, 'index.html')

@login_required
def wild_view(request):
    return render(request, 'wild.html')

@login_required
def warden_view(request):
    return render(request, 'warden.html')

@login_required
def game_park_view(request):
    return render(request, 'game_park.html')


@login_required
def add_warden_view(request):
    message = ''
    if request.method == "POST":
        warden_form= WardenForm(request.POST)

        if warden_form.is_valid():
             warden_form.save()
             message = "addition successful"
             

    warden = Warden.objects.all()
    warden_form = WardenForm()
    


    context ={
        'form':warden_form,
        'msg':message,
        'warden': warden,
    }
    return render(request, 'add_warden.html', context)

@login_required
def add_game_park_view(request):
    message = ''
    if request.method == "POST":
        game_park_form = Game_parkForm(request.POST)

        if game_park_form.is_valid():
            game_park_form.save()
            messages.success(request,"addition successful") 
            

    
    game_park_form = Game_parkForm()
    game_park = Game_park.objects.all()


    context ={
        'form':game_park_form,
        'msg':message,
        'game_park': game_park,
    }
    return render(request, 'add_game_park.html', context)

@login_required
def add_wild_view(request):
    message = ''
    if request.method =="POST":
        wild_form = WildForm(request.POST)

        if wild_form.is_valid():
            wild_form.save()
            messages.success(request,"addition successful") 

    
    wild_form = WildForm()
    wild = Wild.objects.all()

    context ={
        'form':wild_form,
        'msg':message,
        'wild':wild
    }

    return render(request, "add_wild.html", context)

@login_required
def add_visitor_view(request):
    message = ''
    if request.method =="POST":
        visitor_form = VisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor_form.save()
            messages.success(request,"addition successful") 

    
    visitor_form = VisitorForm()
    visitor = Visitor.objects.all()

    context ={
        'form':visitor_form,
        'msg':message,
        'visitor': visitor
    }

    return render(request, "add_visitor.html", context)

@login_required
def add_payment_view(request):
    message = ''
    if request.method =="POST":
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()

            messages.success(request,"addition successful") 

    
    payment_form = PaymentForm()
    payment = Payment.objects.all()

    context ={
        'form':payment_form,
        'msg':message,
        'payment': payment
    }

    return render(request, "add_payment.html", context)


@login_required
def edit_warden_view(request, warden_id):
    message = ''
    warden = Warden.objects.get(id= warden_id)

    if request.method == "POST":
        warden_form = WardenForm(request.POST,request.FILES, instance=warden)

        if warden_form.is_valid():
            warden_form.save()
            message = "saved successfully"

            return redirect(add_warden_view)

        else:
            messages.success(request,"edit successful") 

    else:
        warden_form = WardenForm(instance=warden) 

    context = {
        'form':warden_form,
        'warden':warden,
        'message': message 
    }

    return render(request, "edit_warden.html", context)


    



@login_required
def edit_game_park_view(request, game_park_id):
    message = ''
    game_park = Game_park.objects.get(id= game_park_id)

    if request.method == "POST":
        game_park_form = Game_parkForm(request.POST, instance=game_park)

        if game_park_form.is_valid():
            game_park_form.save()
            messages.success(request,"edit successful")

            return redirect(add_game_park_view)

        else:
            message = "saved data is ivalid"

    else:
        game_park_form = Game_parkForm(instance=game_park) 

    context = {
        'form':game_park_form,
        'game_park':game_park,
        'message': message 
    }

    return render(request, "edit_game_park.html", context)


@login_required
def edit_wild_view(request, wild_id):
    message = ''
    wild = Wild.objects.get(id= wild_id)

    if request.method == "POST":
        wild_form  = WildForm(request.POST, instance= wild)

        if wild_form.is_valid():
            wild_form.save()
            messages.success(request,"edit successful")

            return redirect(add_wild_view)

        else:
            message = "saved data is invalid"

    else:
        wild_form = WildForm(instance= wild) 

    context = {
        'form':wild_form,
        'wild':wild,
        'message': message 
    }

    return render(request, "edit_wild.html", context)

@login_required
def edit_visitor_view(request, visitor_id):
    message = ''
    visitor = Visitor.objects.get(id= visitor_id)

    if request.method == "POST":
        visitor_form = VisitorForm(request.POST, instance=visitor)

        if visitor_form.is_valid():
            visitor_form.save()
            messages.success(request,"edit successful")

            return redirect(add_visitor_view)

        else:
            message = "saved data is invalid"

    else:
        visitor_form = VisitorForm(instance=visitor) 

    context = {
        'form':visitor_form,
        'visitor':visitor,
        'message': message 
    }

    return render(request, "edit_visitor.html", context)

@login_required
def edit_payment_view(request, payment_id):
    message = ''
    payment = Payment.objects.get(id= payment_id)

    if request.method == "POST":
        payment_form = PaymentForm(request.POST, instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            messages.success(request,"edit successful")

            return redirect(add_payment_view)

        else:
            message = "saved data is ivalid"

    else:
        payment_form = PaymentForm(instance=payment) 

    context = {
        'form':payment_form,
        'payment':payment,
        'message': message 
    }

    return render(request, "edit_payment.html", context)
    


@login_required
def delete_warden_view(request, warden_id):
    warden = Warden.objects.get(id= warden_id)

    warden.delete()

    return redirect(add_warden_view)

def delete_game_park_view(request, game_park_id):
    game_park = Game_park.objects.get(id= game_park_id)

    game_park.delete()

    return redirect(add_game_park_view)

def delete_wild_view(request, wild_id):
    wild = Wild.objects.get(id= wild_id)

    wild.delete()

    return redirect(add_wild_view)

def delete_visitor_view(request, visitor_id):
    visitor = Visitor.objects.get(id= visitor_id)

    visitor.delete()

    return redirect(add_visitor_view)

def delete_payment_view(request, payment_id):
    payment = Payment.objects.get(id= payment_id)

    payment.delete()

    return redirect(add_payment_view)

def sign_up_view(request):
    message = ''
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        

        if sign_up_form.is_valid():
            sign_up_form.save()

            message = "sign_up successful"
            
            

        else:
            message = "not successful"

    
    sign_up_form = UserCreationForm()
    


    context ={
        'form':sign_up_form,
        'message':message,
        
    }
    return render(request, 'registration/sign_up.html', context)



