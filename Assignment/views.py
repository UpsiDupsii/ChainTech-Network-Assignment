from django.shortcuts import render
import json
import urllib

# Create your views here.
def index(request):
    
    return render(request, "index.html")

#Exercise-3
def weatherAPI(request):
    if request.method == "POST":
        city = 0
        city = request.POST['city']
        
        #using Openweather API to fetch weather data from json
        source = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metrics&appid=e86e0d7c0176d4b4c7c868f18cdcc55e").read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' , '+ str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°Farenheit',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data={}
    return render(request, "weatherAPI.html", data)

#Exercise-4
def forms(request):
    return render(request, "forms.html")