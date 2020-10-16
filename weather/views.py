from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8256a4112664476d12154f4697e5ca5'
    city = 'trivandrum'
    city_weather = requests.get(url.format(city)).json()

    if url:
        weather = {

            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
    else:
        return HttpResponse('404 ! Page Not Found')

    return render(request, 'index.html', {'weather': weather})
