from django.shortcuts import render, redirect
from .models import Payment

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})

def payment_detail(request, id):
    payment = Payment.objects.get(id=id)
    return render(request, 'payment/payment_detail.html', {'payment': payment})
def payment_create(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        payment_method = request.POST['payment_method']
        transaction_id = request.POST['transaction_id']
        status = request.POST['status']
        payment = Payment.objects.create(amount=amount, payment_method=payment_method, transaction_id=transaction_id, status=status)
        payment.save()
        return redirect('payment_list')
    else:
        return render(request, 'payment/payment_create.html')

def payment_update(request, id):
    payment = Payment.objects.get(id=id)

    if request.method == 'POST':
        amount = request.POST['amount']
        payment_method = request.POST['payment_method']
        transaction_id = request.POST['transaction_id']
        status = request.POST['status']
        payment.amount = amount
        payment.payment_method = payment_method
        payment.transaction_id = transaction_id
        payment.status = status
        payment.save()
        return redirect('payment_list')
    else:
        return render(request, 'payment/payment_update.html', {'payment': payment})

def payment_delete(request, id):
    payment = Payment.objects.get(id=id)
    payment.delete()
    return redirect('payment_list')
