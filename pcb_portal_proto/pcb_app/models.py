from django.db import models
from django.utils import timezone

import datetime


class Order(models.Model):
    date = models.DateTimeField('order_date', auto_now_add=True)
    currency = models.CharField('order_currency', max_length=3)
    total_cost = models.PositiveIntegerField('order_total_cost')
    delivery_country = models.CharField('order_delivery', max_length=3)
    is_paid = models.BooleanField('order_paid')
    is_delivered = models.BooleanField('order_delivered')
    is_fake = models.BooleanField('order_is_fake')

    def __str__(self):
        return "Order #%s for %s" % (self.id, self.date)

    def created_this_month(self):
        return self.date >= timezone.now() - datetime.timedelta(days=30)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    type = models.CharField('item_type', max_length=10)
    quantity = models.SmallIntegerField('item_quantity')

    class Meta:
        abstract = True


class OrderItemPCB(OrderItem):
    size = models.CharField('pcb_item_size', max_length=10)
    material = models.CharField('pcb_item_material', max_length=100)
    thickness = models.FloatField('pcb_item_thickness')
    color = models.CharField('pcb_item_color', max_length=15)

    def __str__(self):
        return "Printed Circuit Board #%s colored: %s" % (self.id, self.color)




