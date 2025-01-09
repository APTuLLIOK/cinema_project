from django import forms
from django.contrib.auth import get_user_model

from .models import Ticket, SeatForSession, Session


class TicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        session_id = kwargs.pop('session_ID')
        super().__init__(*args, **kwargs)
        self.fields['seat_for_session'].queryset = \
            SeatForSession.objects.filter(
                session__id=session_id,
                is_taken=False
            )

    class Meta:
        model = Ticket
        fields = ('seat_for_session',)
