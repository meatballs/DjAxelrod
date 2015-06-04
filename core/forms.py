from django import forms
from .models import Tournament, TournamentDefinition


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    class Meta:
        model = TournamentDefinition
        fields = ['name', 'players']


