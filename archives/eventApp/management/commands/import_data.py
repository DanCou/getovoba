# your_app/management/commands/import_data.py

import pandas as pd
from django.core.management.base import BaseCommand
from eventApp.models import Team, Player, Event  # Import your models
from django.utils.text import slugify

sex_mapping = { "Femme": "F", "Homme": "M" }

class Command(BaseCommand):
    help = 'Import data from an Excel or CSV file and populate the models'

    def add_arguments(self, parser):
        # Adding a command-line argument for the file path
        parser.add_argument('file_path', type=str, help='The path to the file to be imported')
        parser.add_argument('date_string', type=str, help='The date string (YYYY-MM-DD) of the event where the data will be imported')

    def handle(self, *args, **kwargs):
        # Get the file path from command-line arguments
        file_path = kwargs['file_path']
        date_string = kwargs['date_string']

        self.stdout.write(self.style.NOTICE(f'File path : {file_path}'))
        self.stdout.write(self.style.NOTICE(f'Date string : {date_string}'))

        # Get the Event object by date

        event_date = pd.to_datetime(date_string).date()
        events = Event.objects.filter(event_date=event_date)

        if not events.exists():
            self.stdout.write(self.style.ERROR(f'No event found with date: {date_string}'))
            return
        
        event = events.first()
        self.stdout.write(self.style.NOTICE(f'Event found : {event}'))
        self.stdout.write(self.style.NOTICE(f'Importing...'))

        
        
        # Read the data from the provided file (you can support both Excel and CSV)
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Importing teams
        for index, row in df.iterrows():

            team_name = row['Nom Equipe']
            if pd.isna(team_name):
                self.stdout.write(self.style.WARNING(f'Empty team name at row {index}: setting name to "unknown".'))
                team_name = "Unknown"
                # continue  # Skip this row
            # print(team_name)


            slug = slugify(team_name)
            team, team_created = Team.objects.get_or_create(name=slug, event=event)
            
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {Team.objects.count()} teams.'))

        # Importing players

        for index, row in df.iterrows():
            team_name = row['Nom Equipe']
            slug = slugify(team_name)
            team = Team.objects.get(name=slug)

            print(row)

            player, player_created = Player.objects.get_or_create(
                team=team,
                first_name=row['Prénom participant'],
                last_name=row['Nom participant'],
                sex = sex_mapping[row["Genre"]],
                date_of_birth = row['Date de Naissance'],
                phone_number = row['Mobile'],
                club_name = row['Nom Du Club'],
                club_zipcode = row['Code Postal du Club'],
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {Player.objects.count()} players.'))






    # for index, row in df.iterrows():
    #     # Get or create the Team
    #     # print(slugify(row['Nom Equipe']))
    #     # Get or create the Team instance to avoid duplication
    #     team, team_created = Team.objects.get_or_create(slugify(row['Nom Equipe']))
    #     team.save()
        
        # # Get or create the Player instance to avoid duplication
        # player, player_created = Player.objects.get_or_create(
        #     first_name=row['Prénom participant'],
        #     last_name=row['Nom participant'],
        #     sex=sex_mapping[row["Genre"]],
        #     date_of_birth=row['Date de Naissance'],
        #     phone_number=row['Mobile'],
        #     club_name=row['Nom Du Club'],
        #     club_zipcode=row['Code Postal du Club'],
        # )
        
        # if not player_created:
        #     # If the player already exists, you can optionally update fields here
        #     player.phone_number = row['player_phone']  # Update phone number if needed
        #     player.team = team  # Update team association if needed
        #     player.save()
        
        # # Save the player (though .create() does this automatically)
        # player.save()

    # print(f"Imported {df.shape[0]} rows of data into the database.")

def get_event_by_date(event_date):
    try:
        # Use get() to retrieve the Team object by its name
        event = Event.objects.get(event_date=event_date)
        return event
    except Event.DoesNotExist:
        # Handle the case where no team with the given name exists
        print(f"No event found with date: {event_date}")
        return None