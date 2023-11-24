"""
URL configuration for tourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_app.views import index_view, wild_view, warden_view, add_warden_view, add_game_park_view, add_wild_view,add_visitor_view, add_payment_view,edit_warden_view,delete_warden_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index_view, name='index.html'),
    path('wild', wild_view, name='wild.html'),
    path('warden', warden_view, name='warden.html'),

    path('add_warden/', add_warden_view, name="add_warden_page"),
    path('add_game_park/', add_game_park_view, name="add_game_park_page"),
    path('add_wild/', add_wild_view, name ="add_wild_page"),
    path('add_visitor/', add_visitor_view, name ="add_visitor_page"),
    path('add_payment/', add_payment_view, name ="add_payment_page"),
    path('edit_warden/<int:warden_id>/', edit_warden_view, name="edit_warden_page"),
    path('delete_warden/<int:warden_id>/', delete_warden_view, name="delete_warden_page"),


]
