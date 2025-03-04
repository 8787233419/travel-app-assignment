from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from admin_user.models import TravelOption, Booking
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # print(user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user.__dict__)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    travel_options = TravelOption.objects.all()
    return render(request, 'home.html', {'travel_options': travel_options})

@login_required
def book_travel(request, travel_id):
    travel_option = TravelOption.objects.get(travel_id=travel_id)
    if request.method == 'POST':
        num_seats = int(request.POST['num_seats'])
        # print(num_seats)
        total_price = num_seats * travel_option.price
        Booking.objects.create(
            user=request.user,
            travel_option=travel_option,
            num_seats=num_seats,
            total_price=total_price
        )

        # print(travel_option.available_seats)

        travel_option.available_seats -= num_seats
        # print(travel_option.available_seats)
        travel_option.save()

        return redirect('my_bookings')
    return render(request, 'book_travel.html', {'travel_option': travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    if booking.user == request.user:
        booking.status = 'Cancelled'
        # print(booking.num_seats)
        travel_option=booking.travel_option
        travel_option.available_seats +=booking.num_seats
        # print(booking.travel_option.available_seats ,booking.num_seats)
        booking.save()
        travel_option.save()
    return redirect('my_bookings')