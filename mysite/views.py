from django.shortcuts import render
from .models import service


def home(request):
    listOfServices = service.objects.all()
    dataAvailable = False
    if len(listOfServices) > 0:
        dataAvailable = True
    return render(
        request, "home.html", {"isData": dataAvailable, "data": listOfServices}
    )
