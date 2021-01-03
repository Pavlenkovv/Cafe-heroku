from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking

def reserve(request):

    rest = Booking.objects.all()
    # cont = {'res':rest}

    return HttpResponse(f'{rest}')