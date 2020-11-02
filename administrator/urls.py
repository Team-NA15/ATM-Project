from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='admin-home'),
    path('load-add-atm-card', views.loadAddNewATMCard, name = 'load-add-atm-card'),
    path('add-atm-card', views.addNewATMCard, name = 'add-atm-card'), 
    path('atm-machine-status', views.viewATMachineStatus, name = 'view-atm-status'), 
    path('update-atm-card', views.updateATMCard, name = 'update-atm-card'), 
    path('block-atm-card', views.blockATMCard, name = 'block-atm-card'), 
    path('activate-atm-card', views.activateATMCard, name = 'activate-atm-card'), 
    path('reset-pin', views.resetPin, name = 'reset-pin'), 
    path('reset-phone-number',views.resetPhoneNumber, name = 'reset-phone-number'), 
    path('view-transaction-history', views.viewTransactionHistory, name = 'view-transaction-history'), 
    path('update-expiration-date', views.updateExpDate, name = 'update-expiration-date')
]