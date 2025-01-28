from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('vendor/dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('user/dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('no-permission/', no_permission, name='no_permission'),
]
