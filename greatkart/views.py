from django.shortcuts import render
from store.models import Product
def home(request):

    categories = Product.objects.all()

    context = {
        'Products': categories
    }
    return render(request, 'index.html', context)