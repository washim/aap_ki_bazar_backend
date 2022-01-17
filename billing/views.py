from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Invoice, Shipping


def listorders(request):
    orders = Invoice.objects.all()
    context = {
        'orders': orders
    }
    
    return render(request, 'listorders.html', context)


def vieworder(request, pk):
    order = get_object_or_404(Invoice, id=pk)
    context = {
        'order': order
    }
    
    return render(request, 'vieworder.html', context)