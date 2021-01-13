from django.urls import path

from .views import FlightsListView, FlightDetailView
urlpatterns = [
    # /flights/
    path('', FlightsListView.as_view(), name="index"),
    path('<int:flight_id>', FlightDetailView.as_view(), name="flight-detail"),
    path('<int:flight_id>/book/', FlightBookView.as_view(),)
]