from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    Renders the bag.html template to display the contents of the user's shopping bag.
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Adds a product to the shopping bag or updates its quantity if the product is already in the bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjusts the quantity of a product in the shopping bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    current_quantity = bag.get(item_id, 0)

    bag[item_id] = current_quantity + quantity
    messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(reverse('bag:bag'))


def remove_from_bag(request, item_id):
    """
    Removes a product from the shopping bag.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            messages.error(request, 'Item not found in your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


    