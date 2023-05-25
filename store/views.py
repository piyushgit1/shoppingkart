from django.shortcuts import render, get_object_or_404
from store.models import Product, Variation
from category.models import Category
from cart.models import CartItems
from django.http import HttpResponse
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.

def store(request, category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'Products': paged_products,
        'product_counts': product_count,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItems.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        # variation = Variation.objects.filter(product__id=single_product.id)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        # 'variation': variation
    }

    # return HttpResponse(variation.variation_value)
    # exit()

    # check = single_product.variation_set.all()
    # return HttpResponse(check.is_active)
    # exit()
    return render(request, 'store/product-detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name=keyword))
            product_counts = product.count()

    context = {'Products': product,
               'product_counts': product_counts}

    # return HttpResponse(product.product_name)
    # exit()

    return render(request, 'store/store.html', context)
