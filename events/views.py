from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from .forms import EventForm
from .models import Event
import pandas as pd

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

        return context
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Path to your template
    context_object_name = 'event'  # This is the name of the object in the template

    def get_queryset(self):
        # Return all events or filter as needed
        return Event.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the existing context
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        context['teams'] = self.object.teams.all()  # Add teams to the context
        
        return context


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_add.html'  # Specify your template name
    success_url = reverse_lazy('event-list')  # Redirect to event list after successful form submission

    def form_valid(self, form):
        # Get the uploaded file
        # uploaded_file = form.cleaned_data['file']
        # event_slug = slugify(form.cleaned_data['name'] + "-" \
        #                         + str(form.cleaned_data['date'].year) + "-" \
        #                         + form.cleaned_data['city'])

        # try:
        #     call_command('import_data', uploaded_file, event_slug)
        # except Exception as e:
        #     form.add_error('file', f"Error during importing data : {e}")
        #     return self.form_invalid(form)

        return super().form_valid(form)



class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('event-list')  # Redirect to the event list after deletion


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_edit.html'  # Path to your template
    success_url = reverse_lazy('event-list')  # Redirect after successful update
    
    def get_queryset(self):
        # Return all events or filter as needed
        return Event.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
    
    def form_valid(self, form):
        # Get the uploaded file
        uploaded_file = form.cleaned_data['file']

        return super().form_valid(form)
