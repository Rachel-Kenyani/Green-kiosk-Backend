# Create your views here.
from django.shortcuts import render, redirect
from .models import Discount
from .forms import DiscountForm

def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'discounts/discount_list.html', {'discounts': discounts})

def discount_detail(request, id):
    discount = Discount.objects.get(id=id)
    return render(request, 'discounts/discount_detail.html', {'discount': discount})

def upload_discount(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DiscountForm()
    return render(request, 'discounts/upload_discount.html', {'form': form})

def discount_update(request, id):
    discount = Discount.objects.get(id=id)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            discount = form.save()
            return redirect('discounts/discount_detail, id=id')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'discounts/discount_update.html', {'form': form})
