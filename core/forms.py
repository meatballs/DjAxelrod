from django import forms
from axelrod.strategies import _strategies
from .models import Tournament, TournamentDefinition


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    STRATEGIES = _strategies.basic_strategies + _strategies.ordinary_strategies + _strategies.cheating_strategies
    CHOICES = [(a.__name__, a.__name__) for a in STRATEGIES]
    players = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = TournamentDefinition
        fields = ['name', 'players']


