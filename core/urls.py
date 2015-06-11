from django.conf.urls import patterns, url
from .views import (
    HomeView,
    TournamentListView,
    TournamentDetailView,
    TournamentCreateView,
    TournamentUpdateView,
    TournamentResultsView,
    GraphView,
)

urlpatterns = patterns(
    '',
    # urls for Tournament
    url(
        r'^$',
        HomeView.as_view(),
        name='core_home_view'),
    url(
        r'^tournament/$',
        TournamentListView.as_view(),
        name='core_tournament_list'
    ),
    url(
        r'^tournament/create/$',
        TournamentCreateView.as_view(),
        name='core_tournament_create'
    ),
    url(
        r'^tournament/(?P<pk>\d+)/edit/$',
        TournamentDetailView.as_view(),
        name='core_tournament_detail'
    ),
    url(
        r'^tournament/(?P<pk>\d+)/$',
        TournamentUpdateView.as_view(),
        name='core_tournament_update'
    ),
    url(
        r'^tournament/(?P<pk>\d+)/results/$',
        TournamentResultsView.as_view(),
        name='core_tournament_results'
    ),
    url(
        r'^graph_view/$',
        GraphView.as_view(),
        name='core_graph_view'
    ),
)
