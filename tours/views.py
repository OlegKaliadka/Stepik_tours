import random

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render
from django.views import View

from tours.hotels import title, subtitle, description, departures, tours


class MainView(View):

    def get(self, request):
        id_tour = random.sample(range(1, (len(tours) + 1)), k=6)
        main_tours = {}
        for i in id_tour:
            main_tours[i] = tours[i]
        context = {
            'title' : title,
            'subtitle' : subtitle,
            'main_tours' : main_tours,
            'id_tour' : id_tour,
            'departures' : departures
        }
        return render(request, 'main.html', context=context)


class DepartureView(View):

    def get(self, request, departure):
        if departure not in departures.keys():
            raise Http404
        departures_tour = {}
        prices = []
        nights = []
        for id in tours:
            if tours[id]['departure'] == departure:
                departures_tour[id] = tours[id]
                prices.append(tours[id]['price'])
                nights.append(tours[id]['nights'])
        departure_text = departures.get(departure)
        number_tours = len(departures_tour)
        min_price = min(prices)
        max_price = max(prices)
        min_nights = min(nights)
        max_nights = max(nights)
        if number_tours == 1:
            text_tour = 'tour'
        else:
            text_tour = 'tours'
        context = {
            'title': title,
            'subtitle': subtitle,
            'departures_tour': departures_tour,
            'departure_text' : departure_text,
            'number_tours' : number_tours,
            'min_price': min_price,
            'max_price': max_price,
            'min_nights': min_nights,
            'max_nights': max_nights,
            'text_tour' : text_tour
        }
        return render(request, 'departure.html', context=context)


class TourView(View):

    def get(self, request, id):
        if id not in tours.keys():
            raise Http404
        departure = departures.get(tours[id]['departure'])
        context = {
            'title' : title,
            'subtitle' : subtitle,
            'departures' : departure,
            'tour' : tours[id],
        }
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound("Oops, something's broken...")