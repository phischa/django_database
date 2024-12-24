from django.contrib import admin
from .models import Customer, Product, Bill, Order, ProductType

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    list_display = ["first_name", "last_name", "account"]

    #readonly_fields = []

    #prepopulated_fields = {"slug":["first_name", "last_name"]}

    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo"],
            },
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(ProductType)