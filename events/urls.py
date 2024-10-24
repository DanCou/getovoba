from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventDeleteView, EventUpdateView

from . import views

urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),  # URL for listing all events
    path("<int:pk>/", EventDetailView.as_view(), name="event-detail"),  # URL for event details
    path('add/', EventCreateView.as_view(), name='event-add'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),  # URL for deleting an event
    path('edit/<int:pk>/', EventUpdateView.as_view(), name='event-edit'),
]