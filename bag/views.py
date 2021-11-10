from django.shortcuts import render


def view_bag(request):
    """ A view to renders the bag contents and total price """

    return render(request, 'bag/bag.html')