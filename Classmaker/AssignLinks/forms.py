from django import forms
from .models import Availability
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['start_date', 'start_time', 'end_date', 'end_time']
        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(range_from='start_date'),
            'start_time': TimePickerInput(options={"format": "hh:mm"}),
            'end_time': TimePickerInput(options={"format": "hh:mm"})
        }

from django import forms
from .models import Event
from bootstrap_datepicker_plus.widgets import DatePickerInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date']
        widgets = {
            'date': DatePickerInput()
        }
