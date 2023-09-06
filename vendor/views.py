
from django.shortcuts import render, redirect
from .models import Vendor

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

def add_vendor(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        vendor = Vendor.objects.create(name=name, address=address)
        vendor.save()
        return redirect('vendor_list')
    else:
        return render(request, 'vendor/add_vendor.html')

def edit_vendor(request, id):
    vendor = Vendor.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        vendor.name = name
        vendor.address = address
        vendor.save()
        return redirect('vendor_detail, id=id')
    else:
        return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})
