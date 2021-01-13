from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from .models import Flight, Airport, Passenger
from .forms import BookingForm

# Create your views here.
class FlightsListView(ListView):
    template_name = "flights/index.html"
    queryset = Flight.objects.all()
    context_object_name = "flights"

class FlightDetailView(DetailView):
    template_name = "flights/flight_detail.html"
    queryset = Flight.objects.all()
    context_object_name = "flight"

    def get_object(self):
        x = self.kwargs.get("flight_id")
        return get_object_or_404(Flight, id=x)

    # can add additional context data for the template by simply defining wanted models
    # and adding it to the context QueryDict
    def get_context_data(self, *args, **kwargs):
        context = super(FlightDetailView, self).get_context_data(*args,**kwargs)
        selectedFlight = Flight.objects.get(id=self.kwargs.get("flight_id"))
        context["passengers"] = selectedFlight.passengers.all()

        context["non-passengers"] = Passenger.objects.exclude(flights=selectedFlight).all()

        return context
