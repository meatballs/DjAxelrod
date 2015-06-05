from django import forms
from axelrod.strategies import _strategies
from .models import Tournament, TournamentDefinition

ALL_STRATEGIES = (
    _strategies.basic_strategies +
    _strategies.ordinary_strategies +
    _strategies.cheating_strategies
)

STRATEGY_CHOICES = [(a.__name__, a.__name__) for a in ALL_STRATEGIES]


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    players = forms.MultipleChoiceField(
        choices=STRATEGY_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'multiselect'}))

    class Meta:
        model = TournamentDefinition
        fields = ['name', 'players']
