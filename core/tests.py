import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Tournament, TournamentDefinition


def create_tournament(**kwargs):
    defaults = {}
    defaults["status"] = "status"
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
            "status": "status",
            "tournament_definition": create_tournamentdefinition().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tournament(self):
        tournament = create_tournament()
        url = reverse('core_tournament_detail', args=[tournament.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tournament(self):
        tournament = create_tournament()
        data = {
            "status": "status",
            "tournament_definition": create_tournamentdefinition().id,
        }
        url = reverse('core_tournament_update', args=[tournament.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TournamentDefinitionViewTest(unittest.TestCase):
    '''
    Tests for TournamentDefinition
    '''
    def setUp(self):
        self.client = Client()

    def test_list_tournamentdefinition(self):
        url = reverse('core_tournamentdefinition_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tournamentdefinition(self):
        url = reverse('core_tournamentdefinition_create')
        data = {
            "name": "name",
            "players": "players",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tournamentdefinition(self):
        tournamentdefinition = create_tournamentdefinition()
        url = reverse('core_tournamentdefinition_detail', args=[tournamentdefinition.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tournamentdefinition(self):
        tournamentdefinition = create_tournamentdefinition()
        data = {
            "name": "name",
            "players": "players",
        }
        url = reverse('core_tournamentdefinition_update', args=[tournamentdefinition.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


