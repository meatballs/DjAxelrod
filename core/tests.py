from axelrod import strategies
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django.contrib.auth.models import User
from .models import Tournament, TournamentDefinition, CHEATING_NAMES


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
    defaults["noise"] = 1.0
    defaults["repetitions"] = 10
    defaults["turns"] = 1
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

        # Test results json
        results_url = reverse('core_tournament_results', args=[tournament.id])
        results_response = self.client.get(results_url)
        self.assertEqual(results_response.status_code, 200)

        expected_json = {
            'results': [],
            'meta': {
                'cheating_strategies': CHEATING_NAMES
            }
        }
        self.assertJSONEqual(results_response.content, expected_json)
