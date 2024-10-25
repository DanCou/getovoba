from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventDeleteView, EventUpdateView

from . import views

urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),  # URL for listing all events
    path("<slug:slug>/", EventDetailView.as_view(), name="event-detail"),  # URL for event details
    path('add/', EventCreateView.as_view(), name='event-add'),
    path('<slug:slug>/delete/', EventDeleteView.as_view(), name='event-delete'),  # URL for deleting an event
    path('<slug:slug>/edit/', EventUpdateView.as_view(), name='event-edit'),
]