from django.urls import path
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamDeleteView, TeamUpdateView

from . import views

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),  # URL for listing all events
    # path('add/', TeamCreateView.as_view(), name='team-add'),
    path("<slug:slug>/", TeamDetailView.as_view(), name="team-detail"),  # URL for event details
    path('<slug:slug>/delete/', TeamDeleteView.as_view(), name='team-delete'),  # URL for deleting an event
    path('<slug:slug>/edit/', TeamUpdateView.as_view(), name='team-edit'),
]