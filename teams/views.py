from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Team
from django.shortcuts import get_object_or_404
from .forms import TeamForm
from django.urls import reverse_lazy
from events.models import Event

# Create your views here.

class TeamListView(ListView):
    model = Team
    template_name = 'teams/team_list.html'  # Path to your template
    context_object_name = 'teams'  # Name of the context variable to use in the template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the existing context
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        context['total_teams'] = Team.objects.count()  # Add a count of all events

        return context
    
class TeamDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'  # Path to your template
    context_object_name = 'team'  # This is the name of the object in the template

    def get_queryset(self):
        # Return all events or filter as needed
        return Team.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
    
class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/team_add.html'  # Specify your template name
    # success_url = reverse_lazy('event-detail')  # Redirect to event list after successful form submission

    def get_success_url(self):
        return reverse_lazy('event-detail', kwargs={'slug': self.object.event.slug})  # Redirect to the event detail page after successful creation

# class TeamCreateView(CreateView):
#     model = Team
#     fields = ['name']  # Add other fields as needed
#     template_name = 'team_form.html'  # Your template for the form

    def form_valid(self, form):
        event_slug = self.kwargs['event_slug']  # Get the event slug from the URL
        event = Event.objects.get(slug=event_slug)  # Fetch the event
        form.instance.event = event  # Associate the team with the event
        return super().form_valid(form)









class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'teams/team_confirm_delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('team-list')


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/team_edit.html'  # Path to your template
    success_url = reverse_lazy('team-list')  # Redirect after successful update

    def get_queryset(self):
        # Return all events or filter as needed
        return Team.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)