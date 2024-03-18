from django.shortcuts import render
from django.contrib import messages
from .forms import CollaborateForm

# Home view to the collaboration form


def home(request):
    """
    Home view displaying collaboration form.

    This view renders the home.html template and handles the submission
    of collaboration requests. If a POST request is received with valid
    form data, the collaboration request is saved and a success message
    is displayed.

    **Template**
    :template:`home/home.html`

    **Context**
    ``collaborate_form``
        An instance of :form:`your_app_name.CollaborateForm`.
    """
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
