from django.shortcuts import render, get_object_or_404, redirect
from .models import Activities
from .forms import ActivityForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'activity/index.html')


@login_required
def activity_list(request):
    activities = Activities.objects.filter(user=request.user)
    return render(request, 'activity/activity_list.html', {'activities': activities})


@login_required
def add_activity(request):
    if request.method == 'POST':
        activity_form = ActivityForm(data=request.POST)
        if activity_form.is_valid():
            new_form = activity_form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('activity:list')
    else:
        activity_form = ActivityForm()
    return render(request, 'activity/add_activity.html', {'activity_form': activity_form})


@login_required
def edit_activity(request, id):
    activity = get_object_or_404(Activities, id=id)
    if request.method == 'POST':
        edit_form = ActivityForm(request.POST, instance=activity)
        if edit_form.is_valid():
            activity = edit_form.save(commit=False)
            activity.save()
            return redirect('activity:list')
    else:
        edit_form = ActivityForm(instance=activity)
    return render(request, 'activity/edit_activity.html', {'edit_form': edit_form})


@login_required
def delete_activity(request, id):
    activity = get_object_or_404(Activities, id=id)
    activity.delete()
    return redirect('activity:list')















