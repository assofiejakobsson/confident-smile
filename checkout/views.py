from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NYcs2IgkEUJ9Ck873dAwr1VYG2Rn6MwgNijLWrlPRzFgq45Zh1FGpzY99Q6muzlkzH9lvokK9CtXL5758xHQFnc00gQXV9XC7',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)