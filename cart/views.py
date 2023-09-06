from django.shortcuts import render, redirect
from .models import ShoppingCart
from .forms import CartUploadForm

def upload_cart(request):
    if request.method == 'POST':
        form = CartUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=CartUploadForm()
        return render(request, 'cart/upload_cart.html',{'form': form})

def cart_list(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_detail(request, id):
    cart = ShoppingCart.objects.get(id=id)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
  
def edit_cart(request, id):
    cart = ShoppingCart.objects.get(id=id)
    if request.method == "POST":
        form=CartUploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
        return redirect('cart_detail, id=id')
    else:
        form=CartUploadForm(instance=cart)
        return render(request, 'cart/edit_cart.html',{'form': form})
    
