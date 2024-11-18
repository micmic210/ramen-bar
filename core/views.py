from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin)
def home(request):
    return render(request, 'core/home.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')