from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.management import call_command
from django.conf import settings
from .models import Event
from pathlib import Path

@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):
    if created:
        # Action to trigger after the event is created
        print(f"Event '{instance.name}' has been created!")
        call_command('import_data', Path(settings.MEDIA_ROOT, 'uploads', instance.file.path), instance.slug)
