from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from cart.models import ShoppingCart
from order.models import Order
from .serializers import CustomerSerializer, ProductSerializer, CartSerializer,OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class CustomerListView(APIView):

    #show customer list
    def get(self, request):
        #query list of customers
        customers= Customer.objects.all()
        #serialize the data to json format
        serializer=(CustomerSerializer(customers, many=True))
        #render the data
        return Response(serializer.data)
    
# create customer
# serialize data that is created by customer
    def post(self, request):
        serializer=CustomerSerializer(data= request.data)
        #CustomerSerializer validates the data is valid according to  format eg 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# get customer details
class CustomerDetailView(APIView):
    def get(self, request,id, format=None):
        customer = Customer.objects.get(id = id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, id, request,format=None):
        customer = Customer.objects.get(id = id)
        serializer = CustomerSerializer(customer, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, id, request,format=None):
        customer= Customer.objects.get(id=id)
        customer.delete()
        return Response("Customer deleted",status=status.HTTP_204_NO_CONTENT)


# Product models
class ProductListView(APIView):
    #show product list
    def get(self, request):
        #query list of products
        products= Product.objects.all()
        #serialize the data to json format
        serializer=(ProductSerializer(products, many=True))
        #render the data
        return Response(serializer.data)
    
# create product
# serialize data that is created by product
    def post(self, request):
        serializer=ProductSerializer(data= request.data)
        #ProductSerializer validates the data is valid according to  format eg 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# get product details
class ProductDetailView(APIView):
    def get(self, request,id, format=None):
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, id, request,format=None):
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, id, request,format=None):
        product= Product.objects.get(id=id)
        product.delete()
        return Response("Product deleted",status=status.HTTP_204_NO_CONTENT)


# Cart models
class CartListView(APIView):

    #show cart list
    def get(self, request):
        #query list of carts
        carts= ShoppingCart.objects.all()
        #serialize the data to json format
        serializer=(CartSerializer(carts, many=True))
        #render the data
        return Response(serializer.data)
    
# create cart
# serialize data that is created by product
    def post(self, request):
        serializer=CartSerializer(data= request.data)
        #CartSerializer validates the data is valid according to  format eg 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# get cart details
class CartDetailView(APIView):
    def get(self, request,id, format=None):
        cart = ShoppingCart.objects.get(id = id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def put(self, id, request,format=None):
        cart = ShoppingCart.objects.get(id = id)
        serializer = CartSerializer(cart, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, id, request,format=None):
        cart= ShoppingCart.objects.get(id=id)
        cart.delete()
        return Response("Shopping cart deleted",status=status.HTTP_204_NO_CONTENT)
    def post(self, request, id, format=None):
        cart = ShoppingCart.objects.get(id=id)
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)
        cart.add_product(product)

        # Serialize the updated shopping cart.
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
# In this code:

# A new post method is added, which handles adding a product to the shopping cart.
# It retrieves the shopping cart by its id and the product to be added based on the product_id from the request data.
# It then calls a hypothetical add_product method on the cart instance to add the product to the cart. You should implement this method in your ShoppingCart model.
# After adding the product, it serializes the updated shopping cart using the CartSerializer and returns it with a status code of 200 (HTTP_OK).
# If the product is not found, it returns a 404 (HTTP_NOT_FOUND) response.







class OrderListView(APIView):

    #show order list
    def get(self, request):
        #query list of orders
        orders= Order.objects.all()
        #serialize the data to json format
        serializer=(OrderSerializer(orders, many=True))
        #render the data
        return Response(serializer.data)
    
# create order
    def post(self, request):
        serializer=OrderSerializer(data= request.data)
        #OrderSerializer validates the data is valid according to  format eg 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# get cart details
class OrderDetailView(APIView):
    def get(self, request,id, format=None):
        cart = Order.objects.get(id = id)
        serializer = OrderSerializer(cart)
        return Response(serializer.data)
    
    def put(self, id, request,format=None):
        cart = Order.objects.get(id = id)
        serializer = OrderSerializer(cart, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, id, request,format=None):
        cart= Order.objects.get(id=id)
        cart.delete()
        return Response("Order deleted",status=status.HTTP_204_NO_CONTENT)

