from django.contrib import admin
from .models import Order, OrderItemPCB, Vendor, Sku, VendorInventory

admin.site.register(Order)
admin.site.register(OrderItemPCB)
admin.site.register(Vendor)
admin.site.register(Sku)
admin.site.register(VendorInventory)

