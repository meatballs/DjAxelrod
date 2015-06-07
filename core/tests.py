from axelrod import strategies
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django.contrib.auth.models import User
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


@override_settings(
    AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend'])
class TournamentViewTest(TestCase):
    '''
    Tests for Tournament
    '''

    def setUp(self):
        super(TournamentViewTest, self).setUp()
        self.client = Client()
        self.username = "test_user"
        self.password = "test_pass"
        self.user = User.objects.create_user(
            self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        self.assertTrue(self.user.is_authenticated)

    def test_list_tournament(self):
        tournament = create_tournament()
        url = reverse('core_tournament_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        edit_url = reverse('core_tournament_update', args=[tournament.id])
        self.assertIn(edit_url, response.content)

    def test_create_tournament(self):
        url = reverse('core_tournament_create')
        data = {
            "name": "name",
            "players": strategies.basic_strategies[0].name
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_detail_tournament(self):
        tournament = create_tournament()
        url = reverse('core_tournament_detail', args=[tournament.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tournament(self):
        tournament = create_tournament()
        data = {
            "status": Tournament.PENDING,
            "tournament_definition": create_tournamentdefinition().id,
        }
        url = reverse('core_tournament_update', args=[tournament.id])
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
