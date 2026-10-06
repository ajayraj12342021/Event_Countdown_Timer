from urllib import request

from django.shortcuts import redirect, render
from .models import Event
    
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def add_event(request):
    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['date']
        time=request.POST['time']
        event=Event(Event_name=name,date=date,time=time)
        event.save()
        return redirect('home')
    return render(request,'add_event.html')
