from django import forms
from .models import Timer


class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['title', 'hours', 'minutes', 'seconds', 'priority']

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours', 0)
        minutes = cleaned_data.get('minutes', 0)
        seconds = cleaned_data.get('seconds', 0)

        if hours < 0 or minutes < 0 or seconds < 0:
            raise forms.ValidationError("Hours, minutes, and seconds must be positive")

        return cleaned_data
