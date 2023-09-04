from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from TestingSystem.models import Test
from .models import AssignLinkModel, Availability
from .forms import AvailabilityForm


# Create your views here.


def AssignLinkView(request, test_id, test_description):
    test = get_object_or_404(Test, pk=test_id, slug=test_description)
    if request.method == "GET":
        if request.GET.get('assign', None) == 'True':
            return redirect(
                reverse('Assign:showed-assign', kwargs={'test_id': test_id, 'test_description': test_description}))
    return render(request, 'assignlinks/Assign.html')


def ShowLinks(request, test_id, test_description):
    test = get_object_or_404(Test, pk=test_id, slug=test_description)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            formModel = form.save()
            av = Availability.objects.get(pk=formModel.id)
            model = AssignLinkModel(test_foreign=test, assign_link_foreign=av)
            model.save(test.title)
            return redirect(reverse('Assign:copy-link', kwargs={'assign_id':model.id}))
    else:
        form = AvailabilityForm()
    return render(request, 'assignlinks/LinksShow.html', context={'form': form})


def CopyLinks(request, assign_id):
    model = get_object_or_404(AssignLinkModel, pk=assign_id)
    return render(request, 'assignlinks/LinksCopy.html', context={'assign_link':model.slug_field})



from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Assign:event_list')  # Redirect to the list of events
    else:
        form = EventForm()
    return render(request, 'assignlinks/LinksShow.html', {'form': form})
