import json
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field
from axelrod import strategies
from .models import Tournament, TournamentDefinition

ALL_STRATEGIES = (
    strategies.basic_strategies +
    strategies.ordinary_strategies +
    strategies.cheating_strategies
)

ALL_STRATEGY_NAMES = [s.__name__ for s in ALL_STRATEGIES]


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    strategy_fields = ALL_STRATEGY_NAMES

    class Meta:
        model = TournamentDefinition
        fields = [
            'name',
            'turns',
            'repetitions',
            'noise']
        widgets = {
            'noise': forms.NumberInput(attrs={'step': "0.01"})
        }

    def __init__(self, *args, **kwargs):
        initial = {
            'turns': 200,
            'repetitions': 10,
            'noise': 0
        }
        if 'initial' in kwargs:
            initial.update(kwargs.pop('initial'))

        super(TournamentDefinitionForm, self).__init__(
            initial=initial, *args, **kwargs)

        for strategy in self.strategy_fields:
            self.fields[strategy] = forms.IntegerField(initial=0)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-5'

        self.helper.layout = Layout(
            Fieldset(
                'Config',
                'name',
                'turns',
                'repetitions',
                'noise'
            ),
            Fieldset(
                'Players',
                *self.strategy_fields
            ),
            Submit('submit', 'Start Tournament'),
        )

    def save(self, commit=True):
        tournament_definition = super(TournamentDefinitionForm, self).save(
            commit=False)

        players = {
            strategy: self.cleaned_data[strategy] for
            strategy in self.strategy_fields
            if self.cleaned_data[strategy]
        }

        tournament_definition.players = json.dumps(players)

        if commit:
            tournament_definition.save()

        return tournament_definition
