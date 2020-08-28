from django import forms
from bugtrackerapp.models import Ticket, New_User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, initial="")

class TicketForm(forms.Form):
    title = forms.CharField(max_length = 50)
    description = forms.CharField(widget=forms.Textarea)
    
    
