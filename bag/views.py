from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to renders the bag contents and total price """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of a particular product to the shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
