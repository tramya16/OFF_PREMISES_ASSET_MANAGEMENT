from django.urls import path
from . import views
from .views import add_data, geolocation

app_name = 'myapp'
urlpatterns = [
    path('index.html', views.geolocation, name='home-page'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('anomalies.html', views.anomalies, name='anomalies'),
    path('manuals.html', views.manuals, name='manuals'),
    path('spareparts.html', views.spareparts, name='spareparts'),
    path('aboutus.html', views.anomalies, name='anomalies'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('geolocation', views.geolocation, name='geolocation'),
    path('temperature.html',views.temperature,name="temperature"),
    path('voltage.html',views.Voltage,name="voltage"),
    path('t',views.trial,name="voltage"),
    path('current.html', views.Current, name="current"),
    path('', views.add_data, name='add-data'),
    path('firebase.html', views.firebase, name ="fire-base"),

]