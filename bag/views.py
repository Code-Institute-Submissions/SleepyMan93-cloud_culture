from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to renders the bag contents and total price """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of a particular product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(
                    request, f'Updated {nicotine} {product.name} quantity to {bag[item_id]["items_by_nicotine"][nicotine]} ')
            else:
                bag[item_id]['items_by_nicotine'][nicotine] = quantity
                messages.success(
                    request, f'Added {nicotine} {product.name} to your bag') 
        else:
            bag[item_id] = {'items_by_nicotine': {nicotine: quantity}}
            messages.success(
                request, f'Added {nicotine} {product.name} to your bag')    
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the particular product to the shipping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    nicotine = None 
    if 'nicotine_level' in request.POST:
        nicotine = request.POST['nicotine_level']
    bag = request.session.get('bag', {})

    if nicotine:
        if quantity > 0:
            bag[item_id]['items_by_nicotine'][nicotine] = quantity
            messages.success(
                request, f'Updated {nicotine} {product.name} quantity to {bag[item_id]["items_by_nicotine"][nicotine]} ')
        else:
            del bag[item_id]['items_by_nicotine'][nicotine]
            if not bag[item_id]['items_by_nicotine']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {nicotine} {product.name} from your bag')            
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your bag')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove item from the shipping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        nicotine = None 
        if 'nicotine_level' in request.POST:
            nicotine = request.POST['nicotine_level']
        bag = request.session.get('bag', {})

        if nicotine:
            del bag[item_id]['items_by_nicotine'][nicotine]
            if not bag[item_id]['items_by_nicotine']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {nicotine} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Error removing item: (e)')
        return HttpResponse(status=500)
