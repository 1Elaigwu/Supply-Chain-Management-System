# myapp/views.py

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Order, Inventory

def index(request):
    return HttpResponse("Welcome to the Supply Chain Management System!")

def dashboard(request):
    # Add logic to retrieve data and render dashboard template
    return render(request, 'dashboard.html')

def order_tracking(request):
    # Add logic to retrieve data and render order tracking template
    return render(request, 'order_tracking.html')

def inventory_management(request):
    # Add logic to retrieve data and render inventory management template
    return render(request, 'inventory_management.html')

def reports_analytics(request):
    # Add logic to retrieve data and render reports and analytics template
    return render(request, 'reports_analytics.html')

# Define the orders_api view function to handle API requests
def orders_api(request):
    orders = Order.objects.all()  # Fetch all orders from the database
    # Create a list of dictionaries containing order data
    order_data = [{'order_id': order.order_id, 'product_name': order.product_name, 'order_date': order.order_date, 'status': order.status} for order in orders]
    return JsonResponse(order_data, safe=False)  # Return JSON response with order data

# Define a new view function to handle requests to the inventory API
def inventory_api(request):
    # Fetch inventory data from the database
    inventory_data = Inventory.objects.all()

    # Serialize inventory data into JSON format
    serialized_data = [{'product_name': item.product_name, 'quantity': item.quantity} for item in inventory_data]

    # Return JSON response with inventory data
    return JsonResponse(serialized_data, safe=False)
