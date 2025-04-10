import os
import django
from django.db.models import Sum, Q, F
# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


import os
import django

from main_app.models import Product

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def product_quantity_ordered():
    total_quantity_ordered = (Product.objects
                              .available_products()
                              .annotate(total_ordered_quantity=Sum('orderproduct__quantity'))
                              .exclude(total_ordered_quantity=None)
                              .order_by('-total_ordered_quantity'))

    result = []
    for product in total_quantity_ordered:
        result.append(f'Quantity ordered of {product.name}: {product.total_ordered_quantity}')

    return '\n'.join(result)


# Test Code
# print(product_quantity_ordered())


#
# Exam: 03. Ordered Products Per Customer
#
def ordered_products_per_customer():
    order_by_customer = (Order.objects
                         .prefetch_related('orderproduct_set__product__category')
                         .order_by('id'))

    result = []
    for order in order_by_customer:
        result.append(f'Order ID: {order.id}, Customer: {order.customer.username}')

        for order_product in order.orderproduct_set.all():
            result.append(f'- Product: {order_product.product.name}, Category: {order_product.product.category.name}')

    return '\n'.join(result)


# Test Code
# print(ordered_products_per_customer())

#
# Exam: 04. Available Products Prices
#
def filter_products():
    query = Q(is_available=True) & Q(price__gt=3.00)
    products = Product.objects.filter(query).order_by('-price', 'name')
    # products = Product.objects.filter(is_available=True, price__gt=3.00)
    # products = Product.objects.available_products().filter(price__gt=3.00)

    result = []
    for product in products:
        result.append(f'{product.name}: {product.price}lv.')

    return '\n'.join(result)


# Test Code
# print(filter_products())


#
# Exam: 05. Give Discounts
#
def give_discount():
    (Product.objects
     .available_products()
     .filter(price__gt=3.00)
     .update(price=F('price') * 0.7))

    products_after_discount = Product.objects.available_products().order_by('-price', 'name')
    result = []
    for product in products_after_discount:
        result.append(f'{product.name}: {product.price}lv.')

    return '\n'.join(result)
