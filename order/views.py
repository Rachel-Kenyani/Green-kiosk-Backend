from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from payments.models import Payment

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'orders/order_detail.html', {'order': order})

def create_order(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_list')

    return render(request, 'orders/create_order.html', {'form': form})

def pay_order(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        payment = Payment.objects.create(amount=order.total_price)
        order.payment = payment
        order.save()
        return redirect('order_list')

    return render(request, 'orders/pay_order.html', {'order': order})
