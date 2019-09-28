from django.shortcuts import render
from authenticator.models import Venue


# Create your views here.
def book_for(request, id):
    venue = Venue.objects.get(id=id)
    context = {"venue": venue}
    return render(request, "bookings/book_for.html", context)