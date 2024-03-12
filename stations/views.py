import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings

content = []
with open(settings.BUS_STATION_CSV, encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile, delimiter=',')
    for row in rows:
        content.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    stations = paginator.get_page(page_number)

    context = {
        'bus_stations': stations,
        'page': stations
    }
    return render(request, 'stations/index.html', context)
