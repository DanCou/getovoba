from django.urls import path
from .views import PlayerListView, PlayerDetailView, PlayerCreateView, PlayerDeleteView, PlayerUpdateView

from . import views

urlpatterns = [
    path("", PlayerListView.as_view(), name="player-list"),  # URL for listing all events
    path('add/', PlayerCreateView.as_view(), name='player-add'),
    path("<slug:slug>/", PlayerDetailView.as_view(), name="player-detail"),  # URL for event details
    path('<slug:slug>/delete/', PlayerDeleteView.as_view(), name='player-delete'),  # URL for deleting an event
    path('<slug:slug>/edit/', PlayerUpdateView.as_view(), name='player-edit'),
]