from django import forms

from .models import Airport, Flight, Passenger

class BookingForm(forms.ModelForm):
    testNonPass = Passenger.objects.exclude(id=...).all()

    class Meta:
        model = Flight
        fields = [
            ""
        ]
