from django.shortcuts import redirect, render
from django.views.generic import View
from cart.cart import Cart
from .models import OrderItem
from user.models import CustomUser
from .forms import OrderCreateForm



class OrderCreate(View):
    
    def get(self, request, *args, **kwargs):
        context={
            'form':OrderCreateForm(),
        }
        return render(request, 'order/create.html', context)

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        user = str(request.user.id)
        form = OrderCreateForm({'user':user,
                                'address':request.POST['address'],
                                'city':request.POST['city'],
                                'postal_code':request.POST['postal_code'],
                                })
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity']
                                        )
            cart.clear()
            return redirect('home')
        return render(request, 'order/create.html', {'form':form})