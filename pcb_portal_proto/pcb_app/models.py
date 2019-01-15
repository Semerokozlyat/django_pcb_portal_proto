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





