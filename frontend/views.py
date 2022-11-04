from django.shortcuts import render, HttpResponse
import requests 

# Create your views here.
def index(request):
    bored = requests.get("http://www.boredapi.com/api/activity?")
    json_data = bored.json()
    activity = json_data['activity']
    category = json_data['type']
    link = json_data['link']
    return render(request, 'bored/index.html', {
        "activity": activity, 
        "category": category, 
        "link": link
    })
