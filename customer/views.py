from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer/customer_detail.html', {'customer': customer})

def upload_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/upload_customer.html', {'form': form})
  
def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail, id=id')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_edit.html', {'form': form})