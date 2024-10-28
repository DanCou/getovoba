from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
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


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_add.html'  # Specify your template name
    success_url = reverse_lazy('event-list')  # Redirect to event list after successful form submission

    def form_valid(self, form):
        # Get the uploaded file
        uploaded_file = form.cleaned_data['file']

        # Read the uploaded Excel file using pandas
        try:
            df = pd.read_excel(uploaded_file)  # Read the file directly from the uploaded file object
            print("@@@@@@@@@@@@@@@@@@@@")
            print(df.head())  # Print the first few rows for debugging

            # Loop through the DataFrame and create Event instances
            # for _, row in df.iterrows():
            #     # Assuming your DataFrame has the right columns, adjust as necessary
            #     Event.objects.create(
            #         name=row['name'],
            #         players=row['players'],
            #         date=row['date'],
            #         start_time=row['start_time'],
            #         end_time=row['end_time'],
            #         city=row['city'],
            #         location=row['location'],
            #         image=form.cleaned_data['image'],  # Use the uploaded image if necessary
            #         mode=form.cleaned_data['mode'],
            #         file=uploaded_file,  # Store the uploaded file
            #     )
        except Exception as e:
            form.add_error('file', f"Error processing the uploaded file: {e}")
            return self.form_invalid(form)

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

    # def get_object(self, queryset=None):
    #     event = super().get_object(queryset)
    #     print(event.date)  # Debugging line to check the date value
    #     return event
    
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

        # Read the uploaded Excel file using pandas
        try:
            df = pd.read_excel(uploaded_file)  # Read the file directly from the uploaded file object
            print("@@@@@@@@@@@@@@@@@@@@")
            print(df.head())  # Print the first few rows for debugging

            # Loop through the DataFrame and create Event instances
            # for _, row in df.iterrows():
            #     # Assuming your DataFrame has the right columns, adjust as necessary
            #     Event.objects.create(
            #         name=row['name'],
            #         players=row['players'],
            #         date=row['date'],
            #         start_time=row['start_time'],
            #         end_time=row['end_time'],
            #         city=row['city'],
            #         location=row['location'],
            #         image=form.cleaned_data['image'],  # Use the uploaded image if necessary
            #         mode=form.cleaned_data['mode'],
            #         file=uploaded_file,  # Store the uploaded file
            #     )
        except Exception as e:
            form.add_error('file', f"Error processing the uploaded file: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)
