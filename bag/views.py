from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to renders the bag contents and total price """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of a particular product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    nicotine = None 
    if 'nicotine_level' in request.POST:
        nicotine = request.POST['nicotine_level']
    bag = request.session.get('bag', {})

    if nicotine:
        if item_id in list(bag.keys()):
            if nicotine in bag[item_id]['items_by_nicotine'].keys():
                bag[item_id]['items_by_nicotine'][nicotine] += quantity
            else:
                bag[item_id]['items_by_nicotine'][nicotine] = quantity
        else:
            bag[item_id] = {'items_by_nicotine': {nicotine: quantity}}    
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.error(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of the particular product to the shipping bag """

    quantity = int(request.POST.get('quantity'))
    nicotine = None 
    if 'nicotine_level' in request.POST:
        nicotine = request.POST['nicotine_level']
    bag = request.session.get('bag', {})

    if nicotine:
        if quantity > 0:
            bag[item_id]['items_by_nicotine'][nicotine] = quantity
        else:
            del bag[item_id]['items_by_nicotine'][nicotine]
            if not bag[item_id]['items_by_nicotine']:
                bag.pop(item_id)           
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove item from the shipping bag """

    try:
        nicotine = None 
        if 'nicotine_level' in request.POST:
            nicotine = request.POST['nicotine_level']
        bag = request.session.get('bag', {})

        if nicotine:
                del bag[item_id]['items_by_nicotine'][nicotine]
                if not bag[item_id]['items_by_nicotine']:
                    bag.pop(item_id)
        else:
                bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
