from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    path('cash-transfer', views.loadCashTransfer, name = 'cash-transfer'),
    path('cash-withdrawal', views.loadCashWithdrawal, name = 'cash-withdrawal'),
    path('balance-inquiry', views.balanceInquiry, name='balance-inquiry'),
    path('transaction-history', views.transactionHistory, name='transaction-history'),
    path('pin-change', views.loadPinChange, name = 'pin-change'),
    path('phone-number-change', views.loadPhoneNumberChange, name = 'phone-number-change'),
]