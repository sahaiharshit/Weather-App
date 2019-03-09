import requests
from django.shortcuts import render
from decimal import Decimal
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=c10bb3bd22f90d636baa008b1529ee25&fbclid=IwAR2K8aYY5-SXvz9zCYCFHFkKKyvJcMnQ4p_NqAEn9wrHP370aWHy2vSqdj8'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data =[]

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather ={
         'city' : city.name,
         'temprature' : round((r['main']['temp']-273),2),
         'description' :r['weather'][0]['description'] ,
         'icon' :r['weather'][0]['icon'] ,
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)
