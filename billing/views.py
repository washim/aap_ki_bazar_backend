from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice


@login_required
def listorders(request):
    orders = Invoice.objects.all()
    context = {
        'orders': orders
    }
    
    return render(request, 'listorders.html', context)


@login_required
def vieworder(request, pk):
    order = get_object_or_404(Invoice, id=pk)
    context = {
        'order': order
    }
    
    return render(request, 'vieworder.html', context)