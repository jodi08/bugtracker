from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

# Create your models here.

class New_User(AbstractUser):
    pass
    
    def __str__(self):
        return self.username

class Ticket(models.Model):
    new = 'new' 
    inprogress = 'inpr' 
    done = 'done'
    invalid = 'inv'

    CHOICES = [
        (new, 'New'), (inprogress, 'In Progress'), (done, "Done"), (invalid, "Invalid")
    ]
    title = models.CharField(max_length=75)
    time_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(New_User, on_delete=models.CASCADE, related_name="author")
    status = models.CharField(max_length=4, choices=CHOICES, default=new)
    assigned_to = models.ForeignKey(New_User, blank=True, null=True, on_delete=models.CASCADE, related_name="assigned")
    completed = models.ForeignKey(New_User, blank=True, null=True, on_delete=models.CASCADE, related_name="completed")


