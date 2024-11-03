from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Player
from django.shortcuts import get_object_or_404
from .forms import PlayerForm
from django.urls import reverse_lazy

# Create your views here.

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'  # Path to your template
    context_object_name = 'players'  # Name of the context variable to use in the template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the existing context
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        context['players'] = Player.objects.count()  # Add a count of all events

        return context
    
class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'  # Path to your template
    context_object_name = 'player'  # This is the name of the object in the template

    def get_queryset(self):
        # Return all events or filter as needed
        return Player.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
    
class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_add.html'  # Specify your template name
    success_url = reverse_lazy('player-list')  # Redirect to event list after successful form submission

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('team-detail')


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_edit.html'  # Path to your template
    success_url = reverse_lazy('team-detail')  # Redirect after successful update

    def get_queryset(self):
        # Return all events or filter as needed
        return Player.objects.all()

    def get_object(self, queryset=None):
        # Use the provided queryset if it exists, otherwise use the default
        
        queryset = queryset or self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)