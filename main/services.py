from django.shortcuts import render
from user.models import ATMCard
from main.models import Transaction
from administrator.models import Admin
from django.utils import timezone
# from datetime import datetime, date
import datetime


#METHOD TO RENDER PAGES WITH ANY CONTEXT
#ASSUMES THAT PATH HAS BEEN SET PROPERLY
#ASSUMES THAT RENDERDATA OBJECT CONTAINS REQUEST, PATH, AND CONTEXT OBJECT 
def renderPage(renderData): 
    if not renderData['request']: 
        return 'No request provided'
    if not renderData['path']:
        return 'No template path provided'
    if not renderData['context']: 
        return render(renderData['request'], renderData['path'])
    return render(renderData['request'], renderData['path'], renderData['context'])


#METHOD TO RETRIEVE A CARDHOLDER BY THE ATM CARD NUMBER
#@Params: (cardNumber) card number to search for 
#@Returns: If ATMCard found, returns that objects, if not returns string message
def getCardholderByNumber(cardNumber): 
    try: 
        card = ATMCard.objects.get(card_number = cardNumber)
    except: 
        return false
    return card

#METHOD TO RETRIEVE TRANSACTIONS VIA ATM CARDHOLDERS CARD NUMBER
#@Params: (cardNumber) card number associated with transactions
#@Returns: if transactions exist returns all transactions, if no transactions returns string message no transactions
def getTransactionsByCard(cardNumber): 
    try: 
        transactions = Transaction.objects.all().filter(atm_card_number = cardNumber)
    except: 
        return 'Card Number Invalid'
    if len(transactions) == 0: 
        return False
    return transactions


#METHOD TO SET THE MESSAGE OF CONTEXT OBJECT, ASSUMES THE OBJECT ALREADY HAS A MESSAGE PROPERTY
#@Params: (data) the context object containing the message, (message) string message to be added to message property
def setContextMessage(data, message): 
    data['message'] = message
    return


def getAdmin(user): 
    try:
        admin = Admin.objects.get(username = user)
    except: 
        return false
    return admin


def newExpDate(): 
    return timezone.now() + timezone.timedelta(days=1095)


def validatePhoneNumber(phone_number): 
    countCheck = phone_number.count('-')
    if countCheck != 2: 
        return False 
    numberCheck = phone_number.replace('-', '')
    if not numberCheck.isdigit(): 
        return False 
    
    return True

