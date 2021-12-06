from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(product)
    form = CartAddProductForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        cart.add(product=product,
                quantity=form.cleaned_data['quantity'],
                update_quantity=True)
    return redirect('cart_detail')

def cart_detail(request):

    context = {
        'cart': Cart(request),
        'cart_product_form':CartAddProductForm
    }
    return render(request, 'cart/cart_detail.html', context)