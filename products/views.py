from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """ A view to return all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You search produced nothing")
                return redirect(reverse(
                    'products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_details(request, product_id):
    """ 
    A view to return individual products, including details. A 404 error message if not the product
    and render review form for each product
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter()
    new_review = None
    template = 'products/product_details.html'

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            """ Create Review """
            new_review = review_form.save(commit=False)
            """ Assign user to review """
            request.user = new_review.review_user
            new_review.save()
            """ Assign review to product """
            product = new_review.product_id
            new_review.save()

            review_form = ReviewForm()

            messages.success(request, 'Review successfully posted.')
            return redirect(reverse('product_details', args=[product.id]))
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form
    }

    return render(request, template, context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.review_user or request.user.is_superuser:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.success(
                    request, 'Thanks. You have successfully updated your Review')
                return redirect(reverse('product_details'))
            else:
                messages.error(request, 'Error! \
                    Please check your form is valid.')
        else:
            review_form = ReviewForm(instance=review)
            messages.info(request, f'Editing Review \
                "{review.review_title}"')
    else:
        messages.error(request, (
                f'Sorry only user {review.review_user} can edit this review.'))
        return redirect(reverse('product_details'))

    context = {
        'review_form': review_form,
        'review': review,
    }

    return render(request, 'products/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.review_user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review Deleted')
        return redirect(reverse('product_details'))
    else:
        messages.error(request, (
            f'Sorry only {review.review_user} can delete this review'))
        return redirect(reverse('products'))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to perform this action')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product via the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to perform this action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please make sure the form is complete.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete product from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to perform this action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))