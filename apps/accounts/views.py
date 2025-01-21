from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView

class CustomLoginView(LoginView):
    def get_success_url(self):
        # Redirect users based on their role
        if self.request.user.is_vendor():
            return '/vendor/dashboard/'
        elif self.request.user.is_buyer():
            return '/buyer/dashboard/'
        return '/user/dashboard/'

class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return '/accounts/login/'

class VendorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'vendor_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_vendor():
            return redirect('no_permission')
        return super().dispatch(request, *args, **kwargs)

class BuyerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'buyer_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_buyer():
            return redirect('no_permission')
        return super().dispatch(request, *args, **kwargs)

def no_permission(request):
    return render(request, 'no_permission.html')
