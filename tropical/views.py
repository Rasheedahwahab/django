from django.shortcuts import render

def home_view(request):
    return render (request, 'home.html')

def branch_view(request):
    return render (request, 'branch.html')

def account_view(request):
    return render (request, 'account.html')

def transaction_view(request):
    return render (request, 'transaction.html')

def acc_type_view(request):
    return render (request, 'acc_type.html')




