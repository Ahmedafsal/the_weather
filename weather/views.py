from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import requests
from .models import City

def index(request):

    if request.method == 'POST':
        city_name = request.POST['city_name'].upper()
        if not City.objects.filter(name= city_name):
            obj = City(name= city_name)
            obj.save()
            
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8256a4112664476d12154f4697e5ca5'
        cities = City.objects.all()
        weather_data = []

        try:
            if cities:
                for city in cities:
                    city_weather = requests.get(url.format(city.name)).json()
                    weather = {

                        'city': city.name,
                        'temperature': city_weather['main']['temp'],
                        'description': city_weather['weather'][0]['description'],
                        'icon': city_weather['weather'][0]['icon']
                    }

                    weather_data.append(weather)
        except KeyError:
            print("key error")
        except Exception as e:
            print(e)
        return render(request, 'index.html', {'weather_data': weather_data})
    else:
        return render(request, 'index.html')
