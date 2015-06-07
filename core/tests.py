import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Tournament, TournamentDefinition


def create_tournament(**kwargs):
    defaults = {}
    defaults["status"] = Tournament.PENDING
    defaults.update(**kwargs)
    if "tournament_definition" not in defaults:
        defaults["tournament_definition"] = create_tournamentdefinition()
    return Tournament.objects.create(**defaults)


def create_tournamentdefinition(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["players"] = "players"
    defaults.update(**kwargs)
    return TournamentDefinition.objects.create(**defaults)


class TournamentViewTest(unittest.TestCase):
    '''
    Tests for Tournament
    '''
    def setUp(self):
        self.client = Client()

    def test_list_tournament(self):
        url = reverse('core_tournament_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tournament(self):
        url = reverse('core_tournament_create')
        data = {
            "status": Tournament.PENDING,
            "tournament_definition": create_tournamentdefinition().id,
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_detail_tournament(self):
        tournament = create_tournament()
        url = reverse('core_tournament_detail', args=[tournament.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tournament(self):
        tournament = create_tournament()
        data = {
            "status": Tournament.PENDING,
            "tournament_definition": create_tournamentdefinition().id,
        }
        url = reverse('core_tournament_update', args=[tournament.id,])
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

