from django.shortcuts import render, get_object_or_404
from .cart import Cart
from app1.models import Product
from django.http import JsonResponse


# Create your views here.


def CartView(request):
    return render(request, 'CartCart.html')


def AddView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        response = JsonResponse({'product.name': product.name})
        return response


def DeleteView(request):
    pass


def EditView(request):
    pass
