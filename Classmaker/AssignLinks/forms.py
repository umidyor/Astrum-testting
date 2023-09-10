from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import (
    Availability,
    LimitTime,
    DisplayEachQuestion,
    NUMBER_CHOICES,
    TestCompletionModel,
    SendOffOn,
    CreatorEmailSendModel,
    TakerEmailSendModel,
)
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ["start_date", "start_time", "end_date", "end_time"]
        widgets = {
            "start_date": DatePickerInput(),
            "end_date": DatePickerInput(range_from="start_date"),
            "start_time": TimePickerInput(options={"format": "hh:mm"}),
            "end_time": TimePickerInput(options={"format": "hh:mm"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the time zone for the widget
        self.fields["start_time"].widget.attrs["timezone"] = "Asia/Tashkent"


from django import forms
from .models import LimitTime
from datetime import datetime, timedelta
from django.utils import timezone


class LimitTimeForm(forms.ModelForm):
    minute = forms.IntegerField(
        initial=0,
        validators=[MinValueValidator(0), MaxValueValidator(1440)],
        widget=forms.NumberInput(attrs={"class": "limit-class", "required": "true"}),
    )

    class Meta:
        model = LimitTime
        fields = ["minute"]

    def __init__(self, *args, **kwargs) -> None:
        super(LimitTimeForm, self).__init__(*args, **kwargs)

        if "instance" in kwargs and kwargs["instance"] is not None:
            minute = kwargs["instance"].minute
            if minute:
                if minute >= 0:
                    self.fields["minute"].initial = int(minute)
                else:
                    self.fields["minute"].initial = 0
        else:
            self.fields["minute"].initial = 0

    def save(self, commit=True):
        instance = super(LimitTimeForm, self).save(commit=False)
        minute = self.cleaned_data["minute"]

        if minute:
            new_datetime = datetime.now() + timezone.timedelta(minutes=minute)
            instance.limited_datetime = new_datetime
            if commit:
                instance.save()

        return instance


class DisplayEachQuestionForm(forms.ModelForm):
    class Meta:
        model = DisplayEachQuestion
        fields = ["selected_number", "randomize", "must_answer"]

    selected_number = forms.ChoiceField(choices=NUMBER_CHOICES, widget=forms.Select())
    randomize = forms.BooleanField(required=False)
    must_answer = forms.BooleanField(initial=True)


class TestCompletionModelForm(forms.ModelForm):
    pass_mark = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={"required": "true"}),
    )
    send_completed_message = CKEditorUploadingWidget()
    send_not_completed_message = CKEditorUploadingWidget()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the 'content' field as not required
        self.fields["send_completed_message"].required = False
        self.fields["send_not_completed_message"].required = False

    class Meta:
        model = TestCompletionModel
        fields = ["pass_mark", "send_completed_message", "send_not_completed_message"]


class SendOffOnForm(forms.ModelForm):
    class Meta:
        model = SendOffOn
        fields = "__all__"

    off_or_no = forms.BooleanField(initial=True, required=False)


class CreatorEmailSendModelForm(forms.ModelForm):
    class Meta:
        model = CreatorEmailSendModel
        fields = ["email"]
        widgets = {"email": forms.EmailInput(attrs={"class": "creator-email"})}


class TakerEmailSendModelForm(forms.ModelForm):
    class Meta:
        model = TakerEmailSendModel
        fields = "__all__"

    point = forms.BooleanField(initial=False, required=False)
    percentage = forms.BooleanField(initial=False, required=False)
    feedback = forms.BooleanField(initial=False, required=False)
    graded = forms.BooleanField(initial=False, required=False)
    Reveal_correct_Answer = forms.BooleanField(initial=False, required=False)
