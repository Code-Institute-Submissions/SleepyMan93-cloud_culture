from django.contrib import admin
from .models import Order, OrderPerItem


class OrderPerItemAdminInLine(admin.TabularInline):
    model = OrderPerItem
    readonly_fields = ('peritem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderPerItemAdminInLine,)

    readonly_fields = ('order_number',
                        'delivery_cost', 'order_total',
                        'grand_total', 'original_bag', 
                        'stripe_pid')

    fields = ('order_number', 'user_profile', 'full_name', 
                'email', 'phone_number', 'country',
                'postcode', 'town_or_city', 'street_address1',
                'street_address2', 'delivery_cost',
                'order_total', 'grand_total', 'original_bag', 
                'stripe_pid')

    list_display = ('order_number', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    

admin.site.register(Order, OrderAdmin)
