from django.urls import path
from . import views


app_name = 'pcb_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:order_id>/', views.order_details, name='order_details_link'),
    path('orders/<int:order_id>/order_item_add', views.order_item_add, name='order_item_add_link'),
    path('orders/', views.order_list, name='order_list_link'),
]