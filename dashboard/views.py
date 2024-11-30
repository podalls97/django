from django.shortcuts import render
from .models import Transaction

def dashboard(request):
    transactions = Transaction.objects.all()
    total_income = sum(t.amount for t in transactions if t.category == 'INCOME')
    total_expense = sum(t.amount for t in transactions if t.category == 'EXPENSE')
    balance = total_income - total_expense
    return render(request, 'dashboard/dashboard.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    })
