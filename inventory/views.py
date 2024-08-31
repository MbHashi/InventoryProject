from django.shortcuts import render
from .models import Item, Category

def dashboard(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'dashboard.html', context)