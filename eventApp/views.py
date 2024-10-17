# from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.

from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Team, Player


# class TeamDetailView(DetailView):
#     model = Team
#     template_name = 'team_detail.html'
#     context_object_name = 'team'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['players'] = self.object.players.all()  # Fetch players related to the team
#         return context

def index(request):
    return HttpResponse("Hello, world. You're at the events index.")

# List all teams
class TeamListView(ListView):
    model = Team
    template_name = 'EventApp/team_list.html'  # Specify your template for listing teams
    context_object_name = 'teams'  # The name to use in the template context

# View details of a specific team along with its players
class TeamDetailView(DetailView):
    model = Team
    template_name = 'EventApp/team_detail.html'  # Specify your template for team details
    context_object_name = 'team'  # The name to use in the template context

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the players to the context
        context['players'] = self.object.players.all()  # Fetch players related to this team
        return context

# Create a new team
class TeamCreateView(View):
    def get(self, request):
        # Logic for displaying a form to create a new team
        # return render(request, 'EventApp/team_form.html', {'form': form})
        pass

    def post(self, request):
        # Logic for handling form submission to create a new team
        # if form.is_valid():
        #     form.save()
        #     return redirect('team_list')
        pass

# Update an existing team
class TeamUpdateView(View):
    def get(self, request, pk):
        # Logic for displaying a form to update a team
        pass

    def post(self, request, pk):
        # Logic for handling form submission to update a team
        pass

# Delete a team
class TeamDeleteView(View):
    def get(self, request, pk):
        # Logic for confirming deletion of a team
        pass

    def post(self, request, pk):
        # Logic for deleting a team
        pass