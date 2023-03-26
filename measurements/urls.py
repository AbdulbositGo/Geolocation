from django.urls import path

from measurements.views import calculate_distance

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance, name='calculate-distance')
]