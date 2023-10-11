from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Task, Driver, Truck


# Create your views here.
def index(request):
    drivers = Driver.objects.all()
    # return HttpResponse("".join([str(driver) + '<br>' for driver in drivers]))
    return render(request, "delta/drivers.html", {"drivers": drivers})


def get_driver(request, driver_id):
    # # Option 1
    # try:
    #     driver = Driver.objects.get(pk=driver_id)
    #     return render(request, "single_driver.html", {"driver": driver})
    # except Driver.DoesNotExist:
    #     return Http404()

    # Option 2
    driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, "delta/single_driver.html", {"driver": driver})
