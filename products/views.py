from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return all products, including sorting and search queries """

    products = Product.objects.all()

    if request.GET: 
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You search produced nothing")
                return redirect(reverse(
                    'products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_details(request, product_id):
    """ A view to return individual products, including details. A 404 error message if not the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)