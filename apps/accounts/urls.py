from django.urls import path
from .views import CustomLoginView, UserRegistrationView, VendorDashboardView, BuyerDashboardView, no_permission

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('vendor/dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('no-permission/', no_permission, name='no_permission'),
]
