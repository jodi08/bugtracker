from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


from bugtrackerapp.forms import TicketForm, LoginForm
from bugtrackerapp.models import New_User, Ticket

# Create your views here.
@login_required
def index_view(request):
    my_ticket = Ticket.objects.all()
    return render(request, 'index.html', {'ticket': my_ticket})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user: 
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            
    form = LoginForm()
    return render(request, "login.html", {"form": form})

@login_required
def ticket_edit_view(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    if request.method == 'POST':
        ticket = Ticket.objects.get(id=post_id)
        return HttpResponseRedirect(reverse())

    form = TicketForm
    return render(request, 'ticket_form.html', {'form': form})

def ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                author = request.user,
                status = Ticket.new,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, "ticket.html", {"form": form})

def ticket_detail(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {'ticket': my_ticket})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))