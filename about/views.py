from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Create profile if it doesn't exist
        profile = Profile.objects.create(user=request.user)
    return render(request, 'about/profile.html', {'profile': profile})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            # Ensure avatar is set before saving
            if 'avatar' not in request.FILES:
                profile.avatar = 'avatars/default.png'  # Or provide a default value
            profile.save()
            return redirect('profile_view')
    else:
        form = ProfileForm()
    return render(request, 'about/profile.html', {'form': form})
