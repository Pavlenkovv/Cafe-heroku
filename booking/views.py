from django.shortcuts import render
from .models import Booking


def reserve_info(request):

    res_info = Booking.objects.get(pk=1)
    cont = {'res_info': res_info}

    return render(request, 'index.html', context=cont)
