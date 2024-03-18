from django.shortcuts import render
from django.contrib import messages
from .forms import CollaborateForm

# Home view to the collaboration form


def home(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration received! We'll respond in 2 working days.")

    collaborate_form = CollaborateForm()

    return render(request, 'home/home.html',
        {
            "collaborate_form": collaborate_form
        },
    )
