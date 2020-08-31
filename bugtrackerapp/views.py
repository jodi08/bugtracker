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
    my_ticket = Ticket.objects.filter(status="new")
    inpr_ticket = Ticket.objects.filter(status="inpr")
    completed_ticket = Ticket.objects.filter(status="done")
    invalid_ticket = Ticket.objects.filter(status="inv")
    return render(request, 'index.html', {'ticket': my_ticket, 'inpr_ticket': inpr_ticket, 'completed_ticket':completed_ticket, 'invalid_ticket':invalid_ticket})

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
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("tdetails", args=[ticket.id]))

    
    data = {
        "title": ticket.title,
        "description": ticket.description,
    }

    form = TicketForm(initial=data)
    return render(request, 'ticket.html', {'form': form})

def ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, "ticket.html", {"form": form})

def ticket_detail(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {'ticket': my_ticket})

def user_detail(request, user_id):
    a_user = New_User.objects.filter(id=user_id).first()
    assigned_tickets = Ticket.objects.filter(assigned_to=user_id)
    filed_tickets = Ticket.objects.filter(author=user_id)
    completed = Ticket.objects.filter(completed=user_id)
    return render(request, 'user_details.html', {'new_user': a_user, 'assigned_tickets': assigned_tickets, 'filed_tickets': filed_tickets, 'completed_tickets': completed})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def invalid_view(request, post_id):
    post = Ticket.objects.get(id=post_id)
    post.status = "inv"
    post.assigned_to = None
    post.completed = None
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def inprogress_view(request, post_id):
    post = Ticket.objects.get(id=post_id)
    post.status = "inpr"
    post.assigned_to = request.user 
    post.completed = None
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def completed_view(request, post_id):
    post = Ticket.objects.get(id=post_id)
    post.status = "done"
    post.assigned_to = None
    post.completed = request.user
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
