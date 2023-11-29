from django.forms import ModelForm

from tropical.models import Account
from tropical.models import Branch
from tropical.models import Account_type
from tropical.models import Transaction
from tropical.models import Customer


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'



class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'


class Account_typeForm(ModelForm):
    class Meta:
        model = Account_type
        fields = '__all__'


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


