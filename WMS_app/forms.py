from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Contact
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'event_date']
        widgets = {
            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'min': date.today().isoformat(),
            }),
        }

    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']
        if event_date < date.today():
            raise forms.ValidationError("You cannot book for a past date. Please select a future date.")
        return event_date

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']