from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required
def home(request):
    return render(request, 'core/home.html')

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Check for double bookings
            existing_reservations = Reservation.objects.filter(
                date=form.cleaned_data["date"],
                time=form.cleaned_data["time"]
            )
            if existing_reservations.exists():
                messages.error(request, "This time slot is already booked.")
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, "Your reservation has been booked!")
                return redirect("home") # Redirect to home 
    else:
        form = ReservationForm()
    
    return render(request, "core/make_reservation.html", {"form": form})


@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if reservation:
        reservation.delete()
        messages.success(request, "Your reservation has been canceled.")
    else:
        messages.error(request, "You don't have permission to cancel this reservation.")
    return redirect("home") # Redirect to home 