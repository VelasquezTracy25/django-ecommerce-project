from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Item
    template_name = "home.html"

# not needed but commenting for reference
# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home.html", context)


# Renders individual item view
def ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
