from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    TemplateView
)
from .models import Tournament, TournamentDefinition
from .forms import TournamentForm, TournamentDefinitionForm


class HomeView(TemplateView):
    template_name = 'core/home.html'


class TournamentListView(ListView):
    model = Tournament


class TournamentCreateView(CreateView):
    model = Tournament
    form_class = TournamentForm


class TournamentDetailView(DetailView):
    model = Tournament


class TournamentUpdateView(UpdateView):
    model = Tournament
    form_class = TournamentForm
