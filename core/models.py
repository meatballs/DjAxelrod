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
import math


CHEATING_NAMES = [strategy.name for strategy in axelrod.cheating_strategies]


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

    def get_results_url(self):
        return reverse('core_tournament_results', args=(self.id,))

    def to_json(self):
        json_results = []
        if self.results:
            for player,scores in self.results.iteritems():
                json_results.append({"player": player, "scores": scores})

        results = {
            "results": json_results,
            "meta": {
                "definition": self.tournament_definition.to_json(),
                "cheating_strategies": CHEATING_NAMES
            }
        }

        return results

    def run(self):

        if self.status != Tournament.PENDING:
            raise Exception(
                u'[tournament %d, current status: %s] SKIPPED !' % (
                    self.id, self.get_status_display()))

        try:
            self.status = Tournament.RUNNING
            self.save(update_fields=['status', ])

            start = datetime.now()

            players = self.tournament_definition.players.split(',')

            strategies = [
                getattr(axelrod, strategy_str)()
                for strategy_str in players
            ]
            tournament_runner = axelrod.Tournament(
                players=strategies,
                turns=self.tournament_definition.turns,
                repetitions=self.tournament_definition.repetitions,
                noise=self.tournament_definition.noise)
            result_set = tournament_runner.play()


            # This fixes the problems where the scores did not match the player
            # results = [
            #     (player, result_set.normalised_scores[index])
            #     for index, player in enumerate(players)
            # ]

            # This still has the correct scores with the correct players, but the
            # order is not correct
            results = [
                (players[rank], result_set.normalised_scores[rank])
                for rank in result_set.ranking
            ]

            self.results = dict(results)

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

    def to_json(self):

        definition = {
            "turns": self.turns,
            "repetitions": self.repetitions,
            "noise": self.noise,
        }

        return definition
