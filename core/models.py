import json
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import (
    DateTimeField,
    CharField,
    ForeignKey,
    IntegerField,
    TextField,
    FloatField,
)
from jsonfield import JSONField
import axelrod


class Tournament(models.Model):

    PENDING = 0
    RUNNING = 1
    SUCCESS = 2
    FAILED = 3

    STATUS_CHOICES = (
        (PENDING, 'PENDING'),
        (RUNNING, 'RUNNING'),
        (SUCCESS, 'SUCCESS'),
        (FAILED, 'FAILED'),
    )

    # Fields
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    status = IntegerField(choices=STATUS_CHOICES, default=PENDING)
    results = JSONField()

    # Relationship Fields
    tournament_definition = ForeignKey('core.TournamentDefinition',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('core_tournament_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('core_tournament_update', args=(self.id,))

    def run(self):

        if self.status != Tournament.PENDING:
            raise Exception(
                u'[tournament %d, current status: %s] SKIPPED !' % (
                    self.id, self.get_status_display()))

        try:
            self.status = Tournament.RUNNING
            self.save(update_fields=['status', ])

            start = datetime.now()

            players = json.loads(self.tournament_definition.players)

            strategies = []
            for strategy_str, number_of_players in players.items():
                for i in range(0, int(number_of_players or 0)):
                    strategies.append(getattr(axelrod, strategy_str)())

            tournament_runner = axelrod.Tournament(
                players=strategies,
                turns=self.tournament_definition.turns,
                repetitions=self.tournament_definition.repetitions,
                noise=self.tournament_definition.noise)
            result_set = tournament_runner.play()

            self.results = [
                (name, [])
                for name in result_set.ranked_names
            ]
            for irep in range(result_set.repetitions):
                for irank in result_set.ranking:
                    self.results[irank][1].append(
                        result_set.normalised_scores[irank][irep]
                    )

            end = datetime.now()
            duration = (end - start).seconds

            # TODO: save duration
            # self.duration = duration
            self.status = Tournament.SUCCESS
            self.save(update_fields=['status', 'results'])

        except Exception, e:
            raise
            # log errors and set tournament status to aborted
            self.status = Tournament.FAILED
            self.save(update_fields=['status', ])
            # TODO: eventually save error message in model


class TournamentDefinition(models.Model):

    # Fields
    name = CharField(max_length=255)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    turns = IntegerField()
    repetitions = IntegerField()
    noise = FloatField()
    players = TextField()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('core_tournamentdefinition_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('core_tournamentdefinition_update', args=(self.id,))
