from django.shortcuts import render
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.

def home(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
            
    collaborate_form = CollaborateForm()

    return render(request, 'home/home.html',
        {
            "collaborate_form": collaborate_form
        },
    
    )


