from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TeleworkRequest
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login")) 
    return render(request, "mdxtelework/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mdxtelework/login.html", {
                "message" : "Invalid Credentials"
            })
    return render(request, "mdxtelework/login.html")

def logout_view(request):
    logout(request)
    return render(request, "mdxtelework/login.html", {
        "message": "Logged out."
    })

def telework_request(request):
    bench_choices = TeleworkRequest.BENCH_CHOICES
    if request.method == "POST":
        telework_date = request.POST.get('telework-date')
        bench_assigned = request.POST.get('bench-assigned')
        completion_date = request.POST.get('completion-date')
        #note = request.POST.get('note')

        time_blocks = []
        start_times = request.POST.getlist('start-time')
        end_times = request.POST.getlist('end-time')
        activities = request.POST.getlist('activity')
        
        for start_time, end_time, activity in zip(start_times, end_times, activities):
            if start_time and end_time and activity:
                time_blocks.append({'start_time': start_time, 'end_time': end_time, 'activity': activity})
        
        telework_request = TeleworkRequest.objects.create(
            user=request.user,
            date_requested=telework_date,
            completion_date=completion_date,
            bench_assigned=bench_assigned,
            completion_report=time_blocks,
            #note=note
            #other bench reason?
        )
        
        messages.success(request, 'Telework request submitted successfully!')
        return redirect('telework_request')
    return render(request, "mdxtelework/telework_request.html", {'bench_choices': bench_choices})

@login_required
def pending_requests(request):
    user_requests = TeleworkRequest.objects.filter(user=request.user, status='pending')
    return render(request, "mdxtelework/pending_requests.html", {'user_requests': user_requests})

@login_required
def previous_requests(request):
    user_requests = TeleworkRequest.objects.filter(user=request.user, status__in=['approved', 'rejected'])
    return render(request, "mdxtelework/pending_requests.html", {'user_requests': user_requests})
