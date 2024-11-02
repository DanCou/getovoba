# your_app/management/commands/import_data.py

import pandas as pd
from django.core.management.base import BaseCommand
from events.models import Event  # Import your models
from teams.models import Team
from players.models import Player
# from players.model import Player
from django.utils.text import slugify
from utils.utils import normalize_string
from pathlib import Path
import datetime

sex_mapping = { "Femme": "F", "Homme": "M", "nan": "NA" }

class Command(BaseCommand):
    help = 'Import data from an Excel or CSV file and populate the models'

    def add_arguments(self, parser):
        # Adding a command-line argument for the file path
        parser.add_argument('file_path', type=str, help='The path to the file to be imported')
        parser.add_argument('event_slug', type=str, help='The event slug where the data will be imported')

    def handle(self, *args, **kwargs):
        # Get the file path from command-line arguments
        file_path = kwargs['file_path']
        event_slug = kwargs['event_slug']

        self.stdout.write(self.style.NOTICE(f'File path : {file_path}'))
        self.stdout.write(self.style.NOTICE(f'Event slug : {event_slug}'))

        # Get the Event object by slug

        events = Event.objects.filter(slug=event_slug)

        if not events.exists():
            self.stdout.write(self.style.ERROR(f'No event found with slug: {event_slug}'))
            return
        
        event = events.first()
        self.stdout.write(self.style.NOTICE(f'Event found : {event}'))
        self.stdout.write(self.style.NOTICE(f'Importing...'))

        
        
        # Read the data from the provided file (you can support both Excel and CSV)
        df = pd.read_excel(file_path, engine='openpyxl')

        df['Date de Naissance'] = pd.to_datetime(df['Date de Naissance'], format='%d/%m/%Y', errors='coerce').dt.date
        
        # Importing teams
        all_teams = set()
        all_players = set()

        for index, row in df.iterrows():

            team_name = row['Nom Equipe']
            if pd.isna(team_name):
                self.stdout.write(self.style.WARNING(f'Empty team name at row {index}: setting name to "unknown".'))
                team_name = "Unknown"
                # continue  # Skip this row
            # print(team_name)
            all_teams.add( ( normalize_string(team_name), slugify(team_name) ) )

            player_lastname = normalize_string(row["Nom participant"])
            player_firstname = normalize_string(row["Prénom participant"])
            try:
                player_sex = sex_mapping[row["Genre"]]
            except:
                player_sex ="U"
            # player_birthday = datetime.datetime.strptime(row["Date de Naissance"], "%d/%m/%Y")
            player_birthday = row["Date de Naissance"]

            all_players.add( (player_lastname, player_firstname, team_name, player_sex, player_birthday))

        # print(sorted(list(all_teams)))
        
        for name, slug in sorted(list(all_teams)):

            team, team_created = Team.objects.get_or_create(name=name, slug=slug, event=event)

        for p_lastname, p_firstname, t_name, p_sex, p_birthday in sorted(list(all_players)):


            # Get the Event object by slug

            teams = Team.objects.filter(slug=slugify(t_name))

            if not teams.exists():
                self.stdout.write(self.style.ERROR(f'No team found with name: {t_name}'))
                return
            
            current_team = teams.first()

            if pd.isna(p_birthday):
                p_birthday = datetime.datetime.strptime("01/01/1900", "%d/%m/%Y").date()

            print(f"@@@@@@@ {p_lastname} @ {p_firstname} @ {t_name} @ {p_sex} @ {p_birthday}")

            player, player_created = Player.objects.get_or_create(
                lastname = p_lastname,
                firstname = p_firstname,
                sex = p_sex,
                birthday = p_birthday,
                team = current_team,
                slug = slugify(f"{p_firstname}-{p_lastname}")
                ) 
            
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {Player.objects.count()} players in {Team.objects.count()} teams.'))

