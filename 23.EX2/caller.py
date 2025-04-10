import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import necessary Django ORM tools
from django.db.models import Count, F, Q
from django.db.models.functions import Coalesce
from main_app.models import Profile, Product, Order


def get_profiles(search_string=None):
    """
    Retrieves profiles where full_name, email, or phone_number contains the search string (case-insensitive).
    Orders results by full_name.
    """
    if not search_string:
        return ""

    profiles = Profile.objects.annotate(order_count=Count('orders')).filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if not profiles.exists():
        return ""

    return "\n".join([
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.order_count}"
        for p in profiles
    ])


def get_loyal_profiles():
    """
    Retrieves profiles with more than two orders, ordered by number of orders descending.
    Uses the custom Profile manager method `get_regular_customers()`.
    """
    loyal_profiles = Profile.objects.annotate(order_count=Count('orders')).filter(
        order_count__gt=2
    ).order_by('-order_count')

    if not loyal_profiles.exists():
        return ""

    return "\n".join([
        f"Profile: {p.full_name}, orders: {p.order_count}"
        for p in loyal_profiles
    ])


def get_last_sold_products():
    """
    Retrieves products from the latest order, ordered by product name.
    Ignores order completion status.
    """
    latest_order = Order.objects.order_by('-creation_date').first()

    if not latest_order or not latest_order.products.exists():
        return ""

    product_names = latest_order.products.order_by('name').values_list('name', flat=True)

    return f"Last sold products: {', '.join(product_names)}"


def get_top_products():
    """
    Retrieves the top 5 most frequently sold products from all orders.
    Orders them by sales count (descending), then product name (ascending).
    """
    top_products = Product.objects.annotate(
        sales_count=Coalesce(Count('orders'), 0)
    ).filter(sales_count__gt=0).order_by('-sales_count', 'name')[:5]

    if not top_products.exists():
        return ""

    return "Top products:\n" + "\n".join([
        f"{product.name}, sold {product.sales_count} times"
        for product in top_products
    ])


def apply_discounts():
    """
    Applies a 10% discount to orders with more than two products that are not completed.
    Uses the F() object for efficient updates.
    """
    discounted_orders = Order.objects.annotate(product_count=Count('products')).filter(
        is_completed=False,
        product_count__gt=2
    )

    updated_count = discounted_orders.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {updated_count} orders."


def complete_order():
    """
    Retrieves the oldest pending order, marks it as completed, and updates product stock.
    If stock reaches 0, marks the product as not available.
    """
    pending_order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if not pending_order:
        return ""

    # Update stock for each product in the order
    for product in pending_order.products.all():
        if product.in_stock > 0:
            product.in_stock -= 1
            if product.in_stock == 0:
                product.is_available = False  # Mark as unavailable
            product.save()

    # Mark order as completed
    pending_order.is_completed = True
    pending_order.save()

    return "Order has been completed!"
