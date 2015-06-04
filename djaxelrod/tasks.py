import time
from datetime import datetime
from celery import shared_task


@shared_task
def tournament_task(tournament_id):

    # tournament = Tournament.objects.get(id=int(tournament_id))

    if True:
    # if tournament.status != TOURNAMENT_STATUS_QUEUED:
    #     print '[tournament %5d] %s; SKIPPED !' % (tournament.id, tournament.get_status_display())
    # else:
    #     print '[tournament %5d] Start processing (%s)' % (job_id, tournament.method)

        try:

            # #
            # # Set Progess status
            # #
            # tournament.status = TOURNAMENT_STATUS_IN_PROGRESS
            # tournament.save_base(raw=True, update_fields=['status', ])

            #
            # Process specific tournament
            #

            start = datetime.now()
            print 'Some work is going on for tournament [%d] ...' % tournament_id
            time.sleep(5)
            end = datetime.now()
            duration = (end - start).seconds

            #
            # update tournament status
            #

            # tournament.status = TOURNAMENT_STATUS_COMPLETED
            # tournament.error_log = u''
            # tournament.duration = duration
            # tournament.save_base(raw=True, update_fields=['status', 'error_log', 'duration', ])

        except Exception, e:
            # log errors and set tournament status to aborted
            # tournament.status = TOURNAMENT_STATUS_ABORTED
            # tournament.duration = 0
            # tournament.error_log = e.message + '\r\n\r\n' + "\r\n".join(traceback.format_tb(sys.exc_info()[2]))
            # tournament.save_base(raw=True, update_fields=['status', 'error_log', 'duration', ])
            # print '[tournament %5d] %s; ERROR: %s' % (tournament.id, tournament.get_status_display(), tournament.error_log)
            pass

        #print '[tournament %5d] %s; duration: %d sec' % (tournament.id, tournament.get_status_display(), tournament.duration)
        print '[tournament %5d] duration: %d sec' % (tournament_id, duration)
