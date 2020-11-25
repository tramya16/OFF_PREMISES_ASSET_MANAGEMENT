from pyexpat.errors import messages
import logging, requests
import urllib
from django.views.generic import View
from .models import motor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from django.core.serializers import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Context, loader
from django.db.models import Count, Q
from django.shortcuts import render
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def index(request):
    template = loader.get_template("./myapp/index.html")
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template("./myapp/login.html")
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template("./myapp/register.html")
    return HttpResponse(template.render())


def showmotors(request):
    last_five =motor.objects.order_by('-id')[:6]
    allmotors = reversed(last_five)

    context = {'allmotors': allmotors}
    return context


def anomalies(request):
    path = './myapp/anomalies.html'
    data = showmotors(request)
    return render(request, path, data)


def manuals(request):
    template = loader.get_template("./myapp/manuals.html")
    return HttpResponse(template.render())


def spareparts(request):
    template = loader.get_template("./myapp/spareparts.html")
    return HttpResponse(template.render())


def aboutus(request):
    template = loader.get_template("./myapp/aboutus.html")
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template("./myapp/dashboard.html")
    return HttpResponse(template.render())


# def home(request):
#     template = loader.get_template("./charts.html")
#     return HttpResponse(template.render())

def geolocation(request):
    template = "./myapp/index.html"
    loc = loc_data(request)
    return render(request, template, loc)


def temperature(request):
    template = loader.get_template("./myapp/temperature.html")
    return HttpResponse(template.render())


def Current(request):
    template = loader.get_template("./myapp/current.html")
    return HttpResponse(template.render())


def Voltage(request):
    template = loader.get_template("./myapp/voltage.html")
    return HttpResponse(template.render())


def trial(request):
    template = loader.get_template("./myapp/trial.html")
    return HttpResponse(template.render())


def add_data(request):
    motor_data = []
    url = 'https://api.thingspeak.com/channels/984447/feeds.json'
    header = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=header)
    data = r.json()
    count = motor.objects.all().count()
    for i in range(count, (len(data["feeds"]))):
        motor.objects.create(
            mid="m1",
            Temp=float(data["feeds"][i]["field1"]),
            voltage=float(data["feeds"][i]["field2"]),
            current=float(data["feeds"][i]["field3"]),
            x=float(data["feeds"][i]["field4"]),
            y=float(data["feeds"][i]["field5"]),
            z=float(data["feeds"][i]["field6"]),
            status=(data["feeds"][i]["field7"][2:-2]),
        )

    return Response('Data added successfully')


def loc_data(request):
    loc = []
    url = 'https://api.thingspeak.com/channels/984447/feeds.json'
    header = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=header)
    data = r.json()
    # for i in range(len(data["feeds"])):
    #     lat = float(data["feeds"][i]["field7"])
    #     lon = float(data["feeds"][i]["field8"])

    lat = 12.940538;
    lon = 77.566287;

    context = {'lat': lat, 'lon': lon}
    return context


def get(self, request):
    data = example.objects.all()
    context = {'data': data}
    print(data)
    return render(request, './myapp/anomalies.html', context)


def firebase(request):
    return render(request, './myapp/firebase.html')
# Create your views here.
