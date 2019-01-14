from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Order, OrderItemPCB


def index(request):
    index_page_urls = ['order_list_link',]
    context = {
        'index_page_urls': index_page_urls,
    }
    return render(request, 'pcb_app/index.html', context)


def order_list(request):
    latest_orders_list = Order.objects.order_by('pk')[:5]
    context = {
        'latest_orders_list': latest_orders_list,
    }
    return render(request, 'pcb_app/order_list.html', context)


def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
    }
    return render(request, 'pcb_app/order_details.html', context)


def order_item_add(request, order_id):
    order = Order.objects.get(pk=order_id)
    try:
        new_order_item = OrderItemPCB(order=order,
                                      type=request.POST['type'],
                                      quantity=request.POST['quantity'],
                                      size=request.POST['size'],
                                      material=request.POST['material'],
                                      thickness=request.POST['thickness'],
                                      color=request.POST['color'],
                                      )
    except Exception as ex:
        context = {
            'order': order,
            'error_message': "Error on attempt to add new Order Item",
        }
        return render(request, 'pcb_app/order_details.html', context)
    else:
        new_order_item.save()
        return HttpResponseRedirect(reverse('pcb_app:order_details_link', args=(order.id,)))


