from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Uhohh! There's nothing in your bag currently")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jv3lhDlVwf5PVgVKzFo4FEP4ipbmvDNe1XhAfTOQliqk150RiJXEJAzc0xHR57bklU4ISexJ9u7D7tax44Bchgn00J3EJolni',
    }

    return render(request, template, context)