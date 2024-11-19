from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("make-reservation/", views.make_reservation, name="make_reservation"),
    path("cancel-reservation/<int:reservation_id>/", views.cancel_reservation, name="cancel_reservation"),

]