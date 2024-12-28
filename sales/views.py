from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer, Bill

# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    paginate_by = 3 #definiert wie viele Elemente pro Seite angezeigt werden.


class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name=name)