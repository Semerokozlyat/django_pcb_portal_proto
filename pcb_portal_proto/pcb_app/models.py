from django.db import models
from django.utils import timezone

import datetime


class Order(models.Model):
    date = models.DateTimeField('order_date', auto_now_add=True)
    currency = models.CharField('order_currency', max_length=3)
    total_cost = models.FloatField('order_total_cost', default=0.0)
    delivery_country = models.CharField('order_delivery', max_length=3)
    is_paid = models.CharField('order_paid', max_length=30)
    is_delivered = models.CharField('order_delivered', max_length=30)
    is_fake = models.CharField('order_is_fake', max_length=30)

    def __str__(self):
        return "Order #%s for %s" % (self.id, self.date)

    def created_this_month(self):
        return self.date >= timezone.now() - datetime.timedelta(days=30)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku_id = models.CharField('item_sku', max_length=100)
    type = models.CharField('item_type', max_length=10)
    quantity = models.SmallIntegerField('item_quantity', default=1)

    class Meta:
        abstract = True


class OrderItemPCB(OrderItem):
    size = models.CharField('pcb_item_size', max_length=10)
    material = models.CharField('pcb_item_material', max_length=100)
    thickness = models.FloatField('pcb_item_thickness')
    color = models.CharField('pcb_item_color', max_length=15)
    price = models.FloatField('pcb_item_price', default=0.0)

    def __str__(self):
        return "Printed Circuit Board #%s colored: %s" % (self.id, self.color)


class Vendor(models.Model):
    name = models.CharField('vendor_name', max_length=100)
    country = models.CharField('vendor_country', max_length=100)
    currency = models.CharField('vendor_currency', max_length=100)

    def __str__(self):
        return "Vendor: %s" % self.name


class Sku(models.Model):
    id = models.CharField('sku_id', max_length=10, primary_key=True, db_index=True)
    section_name = models.CharField('sku_section_name', max_length=50)
    type_name = models.CharField('sku_type_name', max_length=10)
    value = models.CharField('sku_value', max_length=10)
    description = models.CharField('sku_friendly_description', max_length=100)

    def __str__(self):
        return "SKU #%s: %s - %s (%s)" % (self.id, self.type_name, self.value, self.description)


class VendorInventory(models.Model):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.PositiveIntegerField('inventory_sku_price', default=0)
    reserve = models.SmallIntegerField('inventory_sku_reserve', default=0)  # may be negative = means "requested"
    last_update_time = models.DateTimeField('inventory_sku_last_update_time', auto_now_add=True)

    def __str__(self):
        return "Inventory line: SKU %s of %s with reserve of %s" % (self.sku, self.vendor, self.reserve)









