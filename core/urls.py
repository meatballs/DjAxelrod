from django.conf.urls import patterns, url
from .views import TournamentListView, TournamentDefinitionListView
from .views import TournamentDetailView, TournamentDefinitionDetailView
from .views import TournamentCreateView, TournamentDefinitionCreateView
from .views import TournamentUpdateView, TournamentDefinitionUpdateView

urlpatterns = patterns('')

urlpatterns += patterns('',
    # urls for Tournament
    url(r'^core/tournament/$', TournamentListView.as_view(), name='core_tournament_list'),
    url(r'^core/tournament/create/$', TournamentCreateView.as_view(), name='core_tournament_create'),
    url(r'^core/tournament/detail/(?P<id>\S+)/$', TournamentDetailView.as_view(), name='core_tournament_detail'),
    url(r'^core/tournament/update/(?P<id>\S+)/$', TournamentUpdateView.as_view(), name='core_tournament_update'),
)

urlpatterns += patterns('',
    # urls for TournamentDefinition
    url(r'^core/tournamentdefinition/$', TournamentDefinitionListView.as_view(), name='core_tournamentdefinition_list'),
    url(r'^core/tournamentdefinition/create/$', TournamentDefinitionCreateView.as_view(), name='core_tournamentdefinition_create'),
    url(r'^core/tournamentdefinition/detail/(?P<id>\S+)/$', TournamentDefinitionDetailView.as_view(), name='core_tournamentdefinition_detail'),
    url(r'^core/tournamentdefinition/update/(?P<id>\S+)/$', TournamentDefinitionUpdateView.as_view(), name='core_tournamentdefinition_update'),
)

