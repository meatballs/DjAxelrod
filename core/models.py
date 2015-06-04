from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import TextField


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
            raise Exception(u'[tournament %d, current status: %s] SKIPPED !' % (
                self.id, self.get_status_display()))

        try:
            self.status = Tournament.RUNNING
            self.save(update_fields=['status', ])

            start = datetime.now()

            # TODO: replace with real work
            print 'Some work is going on for tournament [%d] ...' % self.pk
            import time
            time.sleep(5)

            end = datetime.now()
            duration = (end - start).seconds

            # TODO: save duration
            #self.duration = duration
            self.status = Tournament.SUCCESS
            self.save(update_fields=['status', ])

        except Exception, e:
            # log errors and set tournament status to aborted
            self.status = Tournament.FAILED
            self.save(update_fields=['status', ])
            # TODO: eventually save error message in model


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


