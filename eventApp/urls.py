from django.urls import path
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('teams/list', TeamListView.as_view(), name='team_list'),  # List all teams
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),  # View details of a specific team
    path('teams/create/', TeamCreateView.as_view(), name='team_create'),  # Create a new team
    path('teams/<int:pk>/update/', TeamUpdateView.as_view(), name='team_update'),  # Update an existing team
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),  # Delete a team
]