from django.shortcuts import redirect
from functools import wraps
from .auth_helpers import is_free_user, is_premium_user, is_admin_user

def free_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not is_free_user(request.user):
            return redirect('landing')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def premium_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        if is_premium_user(user) or is_admin_user(user):
            return view_func(request, *args, **kwargs)
        # Usuario autenticado pero no premium ni admin
        return redirect('upgrade')
    return _wrapped_view

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not is_admin_user(user):
            return redirect('landing')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
