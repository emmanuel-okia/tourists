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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from my_app.views import index_view, wild_view, warden_view, add_warden_view, add_game_park_view, add_wild_view,edit_payment_view,add_visitor_view,edit_visitor_view,delete_payment_view, add_payment_view,edit_warden_view, edit_game_park_view,edit_wild_view,delete_warden_view,delete_game_park_view,delete_visitor_view,delete_wild_view,sign_up_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index_view, name='index.html'),
    path('wild', wild_view, name='wild.html'),
    path('warden', warden_view, name='warden.html'),

    path('add_warden/', add_warden_view, name="add_warden_page"),
    path('add_game_park/', add_game_park_view, name="add_game_park_page"),
    path('add_wild/', add_wild_view, name ="add_wild_page"),
    path('sign_up/', sign_up_view, name ="sign_up_page"),
    path('accounts/', include('django.contrib.auth.urls') ),

    path('add_visitor/', add_visitor_view, name ="add_visitor_page"),
    path('add_payment/', add_payment_view, name ="add_payment_page"),
    path('edit_warden/<int:warden_id>/', edit_warden_view, name="edit_warden_page"),
    path('edit_game_park/<int:game_park_id>/', edit_game_park_view, name="edit_game_park_page"),
    path('edit_wild/<int:wild_id>/', edit_wild_view, name="edit_wild_page"),
    path('edit_visitor/<int:visitor_id>/', edit_visitor_view, name="edit_visitor_page"),
    path('edit_payment/<int:payment_id>/', edit_payment_view, name="edit_payment_page"),
    path('delete_warden/<int:warden_id>/', delete_warden_view, name="delete_warden_page"),
    path('delete_game_park/<int:game_park_id>/', delete_game_park_view, name="delete_game_park_page"),
    path('delete_wild/<int:wild_id>/', delete_wild_view, name="delete_wild_page"),
    path('delete_visitor/<int:visitor_id>/', delete_visitor_view, name="delete_visitor_page"),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name="delete_payment_page"),

  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)