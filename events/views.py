from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import EventForm
from .models import Event

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'  # Path to your template
    context_object_name = 'events'  # Name of the context variable to use in the template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the existing context
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        context['total_events'] = Event.objects.count()  # Add a count of all events
        context['greeting'] = "Tournois VBCG"  # Custom greeting message

        return context
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Path to your template
    context_object_name = 'event'  # This is the name of the object in the template

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Event.objects.get(slug=slug)


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_add.html'  # Specify your template name
    success_url = reverse_lazy('event-list')  # Redirect to event list after successful form submission



class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('event-list')  # Redirect to the event list after deletion


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_edit.html'  # Path to your template
    success_url = reverse_lazy('event-list')  # Redirect after successful update

    def get_object(self, queryset=None):
        event = super().get_object(queryset)
        print(event.date)  # Debugging line to check the date value
        return event
