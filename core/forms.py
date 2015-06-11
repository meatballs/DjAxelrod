from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from axelrod import strategies
from .models import Tournament, TournamentDefinition

ALL_STRATEGIES = (
    strategies.basic_strategies +
    strategies.ordinary_strategies +
    strategies.cheating_strategies
)

ALL_STRATEGY_NAMES = [s.__name__.lower() for s in ALL_STRATEGIES]


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    turns = forms.IntegerField(initial=200)
    repetitions = forms.IntegerField(initial=10)
    noise = forms.FloatField(
        initial=0,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )

    strategy_fields = ALL_STRATEGY_NAMES

    class Meta:
        model = TournamentDefinition
        fields = [
            'name',
            'turns',
            'repetitions',
            'noise',
            'players']

    def __init__(self, *args, **kwargs):
        super(TournamentDefinitionForm, self).__init__(*args, **kwargs)

        for strategy in self.strategy_fields:
            self.fields[strategy] = forms.IntegerField(initial=0)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Start Tournament'))

    def clean_players(self):
        return ",".join(self.cleaned_data['players'])
