from django.shortcuts import render,redirect
from django.contrib import messages

from tropical.forms import AccountForm
from tropical.models import Account
from tropical.forms import BranchForm
from tropical.models import Branch
from tropical.forms import Account_typeForm
from tropical.models import Account_type
from tropical.models import Transaction
from tropical.models import Customer
from tropical.forms import TransactionForm
from tropical.forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render (request, 'home.html')

@login_required
def add_branch_view(request):
    message = ''
    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        
        if branch_form.is_valid():
             branch_form.save()
            


             messages.success(request,"Branch added sucessfully")

    else:
        branch_form = BranchForm() 

       

    branch = Branch.objects.all()

    context = {
        'form': branch_form,
        'msg': message,
        'branch': branch,

    }    
     
    return render(request,"branch.html",context) 
@login_required
def edit_branch_view(request,branch_id):
    message=''
    branch = Branch.objects.get(id=branch_id)

    if request.method == "POST":
        branch_form = BranchForm(request.POST,instance=branch)
        if branch_form.is_valid():
            branch_form.save()
            message.success(request,"changes saved successfully")
            return redirect(add_account_view)
        else:
            message = "form has invalid data"

    else:
        branch_form = BranchForm(instance = branch)

    context={
    'form': branch_form,
    'branch':branch,
    'message':message
    }

    return render(request,'edit_branch.html',context)
@login_required
def delete_add_branch_view(request,branch_id):
    branch = Branch.objects.get(id = branch_id)
    branch.delete()

    return redirect(add_branch_view)
    


@login_required
def add_acc_type_view(request):
    message = ''
    if request.method == "POST":
        acc_form = Account_typeForm(request.POST)
        
        if acc_form.is_valid():
             acc_form.save()
            


             messages.success(request,"account type added sucessfully")

    else:
        acc_form = Account_typeForm() 

       

    acc = Account_type.objects.all()

    context = {
        'form': acc_form,
        'msg': message,
        'acc': acc,

    }    
     
    return render(request,"acc_type.html",context) 

@login_required
def edit_acc_view(request,account_type_id):
    message=''
    acc = Account_type.objects.get(id=account_type_id)

    if request.method == "POST":
        acc_form = Account_typeForm(request.POST,instance=acc)
        if acc_form.is_valid():
            acc_form.save()
            message.success(request,"changes saved successfully")
            return redirect(add_account_view)
        else:
            message = "form has invalid data"

    else:
        acc_form = Account_typeForm(instance = acc)

    context={
    'form': acc_form,
    'acc':acc,
    'message':message
    }

    return render(request,'edit_acc.html',context)

@login_required
def delete_add_acc_view(request,account_type_id):
    acc = Account_type.objects.get(id = account_type_id)
    acc.delete()

    return redirect(add_acc_type_view)
    




@login_required
def add_account_view(request):
    message = ''
    if request.method == "POST":
        account_form = AccountForm(request.POST , request.FILES)
        
        if account_form.is_valid():
             account_form.save()
            


             message = "Account added sucessfully"

    else:
        account_form = AccountForm() 

       

    account = Account.objects.all()

    context = {
        'form': account_form,
        'msg': message,
        'account': account,

    }    
     
    return render(request,"add_account.html",context) 

@login_required
def edit_add_account_view(request,account_id):
    message=''
    account = Account.objects.get(id=account_id)

    if request.method == "POST":
        account_form = AccountForm(request.POST, request.FILES, instance=account)
        if account_form.is_valid():
            account_form.save()
            message.success(request,"changes saved successfully")
            return redirect(add_account_view)
        else:
            message = "form has invalid data"

    else:
        account_form = AccountForm(instance = account)

    context={
    'form': account_form,
    'account':account,
    'message':message
    }


    return render(request,'edit_add_account.html',context)

@login_required
def delete_add_account_view(request,account_id):
    account = Account.objects.get(id = account_id)
    account.delete()

    return redirect(add_account_view)


@login_required
def add_transaction_view(request):
    message = ''
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)
        
        if transaction_form.is_valid():
             transaction_form.save()
            


             messages.success(request,"Transaction added sucessfully")

    else:
        transaction_form = TransactionForm() 

       

    transaction = Transaction.objects.all()

    context = {
        'form': transaction_form,
        'msg': message,
        'transaction': transaction,

    }    
     
    return render(request,"transaction.html",context) 

@login_required
def edit_transaction_view(request,transaction_id):
    message=''
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method == "POST":
        transaction_form = TransactionForm(request.POST,instance=transaction)
        if transaction_form.is_valid():
            transaction_form.save()
            message.success(request,"changes saved successfully")
            return redirect(add_account_view)
        else:
            message = "form has invalid data"

    else:
        transaction_form = TransactionForm(instance = transaction)

    context={
    'form': transaction_form,
    'transaction':transaction,
    'message':message
    }

    return render(request,'edit_transaction.html',context)

@login_required
def delete_transaction_view(request,transaction_id):
    transaction = Transaction.objects.get(id = transaction_id)
    transaction.delete()

    return redirect(add_transaction_view)


def add_customer_view(request):
    message = ''
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        
        if customer_form.is_valid():
             customer_form.save()
            


             message.success(request,"Customer added sucessfully")

    else:
        customer_form = CustomerForm() 

       

    customer = Customer.objects.all()

    context = {
        'form': customer_form,
        'msg': message,
        'customer': customer,

    }    
     
    return render(request,"customer.html",context) 

@login_required
def edit_customer_view(request,customer_id):
    message=''
    customer = Customer.objects.get(id=customer_id)

    if request.method == "POST":
        customer_form = CustomerForm(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            message.success(request,"changes saved successfully")
            return redirect(add_account_view)
        else:
            message = "form has invalid data"

    else:
        customer_form = CustomerForm(instance = customer)

    context={
    'form': customer_form,
    'customer':customer,
    'message':message
    }

    return render(request,'edit_customer.html',context)

@login_required
def delete_customer_view(request,customer_id):
    customer = Customer.objects.get(id = customer_id)
    customer.delete()

    return redirect(add_customer_view)
    


def sign_up_view(request):
    message = ''
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message.success(request,'user created successfully')
        else:
            message = 'something went wrong'

    else:
        sign_up_form = UserCreationForm()

    context = {
    'form':sign_up_form,
    'message':message

    }
    return render(request,'registration/sign_up.html',context)

    

