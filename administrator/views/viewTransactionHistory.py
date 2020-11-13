from main.models import Transaction
from ..forms import ModCardForm
from main.services import renderPage, getCardholderByNumber, setContextMessage, getTransactionsByCard
from user.models import ATMCard



#Request to view transaction history of the ATM, there may be many transactions so a new page for this would work better 
def viewTransactionHistory(request): 
    renderData = {
        'request': request, 
        'path': 'administrator/view-transaction-history.html', 
        'context': {
            'form': ModCardForm(), 
            'message': '', 
            'history': []
        }
    }
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid():
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            #if card is a string it's an error message 
            if isinstance(card, str):
                print(card)
                setContextMessage(renderData['context'], card)
                return renderPage(renderData)
            
            transactions = getTransactionsByCard(form.cleaned_data['card_number'])
            #if transactions is a string it's an error message
            if isinstance(transactions, str): 
                setContextMessage(renderData['context'], transactions)
                return renderPage(renderData)
            
            renderData['context']['history'] = transactions
            return renderPage(renderData)
        else: 
            renderData['context']['message'] = 'Form is invalid'
            return renderPage(renderData)
    else: 
        return renderPage(renderData)