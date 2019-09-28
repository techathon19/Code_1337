from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from authenticator.models import Venue, Booking
from datetime import datetime
# Create your views here.

def hours_between(start_time, end_time):
    return end_time - start_time

def check_conflict(start_time, end_time, venue):
    return False

def perform_booking(request, venue):
    date = request.POST.get('date')
    start_time = datetime.strptime(request.POST.get('start_time'),"%H:%M")
    end_time = datetime.strptime(request.POST.get('end_time'),"%H:%M")
    if(start_time>end_time):
        messages.add_message(request, messages.ERROR, "start-time must be before end-time")
    else:
        messages.add_message(request, messages.ERROR, "start-time is before end-time")
    
    if check_conflict(start_time, end_time, venue):
        messages.add_message(request, messages.ERROR, "Sorry The Hall is not available at the requested time")
    else:
        amount = venue.price_per_hour
        # amount("_____________________________________________")
        print(amount)
        amount *= hours_between(start_time, end_time).seconds//3600
        print(amount)
        tax = 18
        discount = 0
        Booking.objects.create(venue=venue, consumer=request.user.consumer, amount=amount, tax=tax, discount=discount)
    return redirect(request.META.get('HTTP_REFERER'))
    




def book_for(request, id):
    venue = Venue.objects.get(id=id)
    if request.method=='POST':
        return perform_booking(request, venue)
    context = {"venue": venue}
    return render(request, "bookings/book_for.html", context)


def view_bookings(request):
    return render(request, "bookings/view.html", {})