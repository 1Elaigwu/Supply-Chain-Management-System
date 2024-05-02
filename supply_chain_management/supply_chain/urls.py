"""
URL configuration for supply_chain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from inventory_management import views  # Adjust this import based on your app name
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Add this line for the root URL
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order_tracking/', views.order_tracking, name='order_tracking'),
    path('inventory_management/', views.inventory_management, name='inventory_management'),
    path('reports_analytics/', views.reports_analytics, name='reports_analytics'),
    # Add the new URL pattern for the API endpoint
    path('api/orders/', views.orders_api, name='orders_api'),
    path('api/inventory/', views.inventory_api, name='inventory_api'),  # New URL pattern for inventory API
]

urlpatterns += staticfiles_urlpatterns()


