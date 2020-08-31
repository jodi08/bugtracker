"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bugtrackerapp import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('ticket/', views.ticket_view, name="ticket"),
    path('logout/', views.logout_view, name="logout"),
    path('tdetails/<int:ticket_id>/', views.ticket_detail, name="tdetails"),
    path('userdetails/<int:user_id>/', views.user_detail, name="userdetails"),
    path('edit_ticket/<int:post_id>/', views.ticket_edit_view),
    path('invalid/<int:post_id>/', views.invalid_view),
    path('inprogress/<int:post_id>/', views.inprogress_view),
    path('complete/<int:post_id>/', views.completed_view),
    path('admin/', admin.site.urls),
]
