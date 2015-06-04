from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import TextField


class Tournament(models.Model):

    STATUS_CHOICES = (
        (0, 'PENDING'),
        (1, 'RUNNING'),
        (2, 'SUCCESS'),
        (3, 'FAILED'),
    )

    # Fields
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    status = IntegerField(choices=STATUS_CHOICES)

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


class TournamentDefinition(models.Model):

    # Fields
    name = CharField(max_length=255)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    players = TextField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('core_tournamentdefinition_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('core_tournamentdefinition_update', args=(self.id,))


