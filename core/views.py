from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    TemplateView
)
from django.core.urlresolvers import reverse
from .models import Tournament, TournamentDefinition
from .forms import TournamentForm, TournamentDefinitionForm


class HomeView(TemplateView):
    template_name = 'core/home.html'


class TournamentListView(ListView):
    model = Tournament


class TournamentCreateView(CreateView):
    model = TournamentDefinition
    form_class = TournamentDefinitionForm
    template_name = 'core/tournament_form.html'
    tournament = None

    def form_valid(self, form):
        self.object = form.save()
        self.tournament = Tournament.objects.create(tournament_definition=self.object)
        self.tournament.save()

        return super(TournamentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('core_tournament_update', args=(self.tournament.id,))


class TournamentDetailView(DetailView):
    model = Tournament


class TournamentUpdateView(UpdateView):
    model = Tournament
    form_class = TournamentForm
