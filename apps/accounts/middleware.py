from django.shortcuts import redirect

class RoleBasedRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/vendor') and not request.user.is_vendor():
            return redirect('no_permission')
        elif request.path.startswith('/buyer') and not request.user.is_buyer():
            return redirect('no_permission')
        return self.get_response(request)
