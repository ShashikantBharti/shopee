from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm
from django.views.generic.list import ListView

class ProductUploadView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/upload_product.html'

    def form_valid(self, form):
        # Automatically assign the logged-in user as the vendor
        form.instance.vendor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/products/'  # Redirect to a product listing page after upload
    
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Filter products by the logged-in vendor
        return Product.objects.filter(vendor=self.request.user)
