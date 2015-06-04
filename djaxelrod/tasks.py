from celery import shared_task
from core.models import Tournament


@shared_task
def tournament_task(tournament_id):

    print u'[tournament %d] Start running' % tournament_id
    tournament = Tournament.objects.get(id=int(tournament_id))
    tournament.run()
    print u'[tournament %d] %s End running' % (
        tournament.id, tournament.get_status_display())
