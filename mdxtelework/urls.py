from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("telework_request", views.telework_request, name="telework_request"),
    path("pending_requests", views.pending_requests, name="pending_requests"),
    path("previous_requests", views.previous_requests, name="previous_requests"),
]