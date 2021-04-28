from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
    

@login_required
def add_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user.id)
        messages.success(request, f'Removed {product.name} from your wishlist')
    else:
        product.wishlist.add(request.user.id)
        messages.success(request, f'Added {product.name} to your wishlist')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def wishlist(request):
    products = Product.objects.filter(wishlist=request.user.id)
    items = {'wishlist': products}
    print(products)
    return render(request, 'profiles/wishlist.html', items)
