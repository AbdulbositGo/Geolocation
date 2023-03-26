from django.shortcuts import render, get_object_or_404

from measurements.forms import MeasurementModelForm
from measurements.models import Measurement


def calculate_distance(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm()

    context = {
        'distance': obj,
        'form': form
    }
    return render(request, 'measurements/main.html', context)
