from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.views.generic.list import ListView
from django.http import HttpResponseForbidden

class ProductUploadView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/upload_product.html'

    def dispatch(self, request, *args, **kwargs):
        # Restrict access to vendors only
        if not request.user.is_vendor():
            return HttpResponseForbiddenWithTemplate(request)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Automatically assign the logged-in user as the vendor
        form.instance.vendor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/products/'  # Redirect to product listing after upload
    
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def dispatch(self, request, *args, **kwargs):
        # Restrict access to vendors only
        if not request.user.is_vendor():
            return HttpResponseForbiddenWithTemplate(request)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Filter products by the logged-in vendor
        return Product.objects.filter(vendor=self.request.user)
    
def HttpResponseForbiddenWithTemplate(request):
    return render(request, '403.html', status=403)
