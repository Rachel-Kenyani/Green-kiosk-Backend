from django.shortcuts import render,redirect
from .forms import ProductUploadForm
from inventory.models import Product
from cart.models import ShoppingCart

def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})

   
def product_list(request):
    products=Product.objects.all()
    return render(request,'inventory/product_list.html',{'products':products})
    
def  product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'inventory/product_detail.html',{'product':product})


def product_view(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=Product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view",id=Product.id )
    else:
        form = ProductUploadForm(instance=product)

    return render(request, "inventory/edit_product.html", {"form": form})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart= ShoppingCart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart_list')
    return render(request, 'cart/cart_list.html', {'carts': carts})
# return redirect('cart_detail, id=id')

# def add_to_cart(request, product_id): 
#     product = Product.objects.get(id=product_id)
#     cart= ShoppingCart.objects.get_or_create(user=request.user)
#     cart.products.add(product)
#     return redirect('cart_list')
#     return render(request, 'cart/cart_list.html', {'carts': carts})
# return redirect('cart_detail, id=id')
