from django.contrib import admin
from django import forms
from .models import Tournament, TournamentDefinition

class TournamentAdminForm(forms.ModelForm):

    class Meta:
        model = Tournament
        exclude = []


class TournamentAdmin(admin.ModelAdmin):
    form = TournamentAdminForm
    list_display = ['created', 'last_updated', 'status']
    readonly_fields = ['created', 'last_updated', 'status']

admin.site.register(Tournament, TournamentAdmin)


class TournamentDefinitionAdminForm(forms.ModelForm):

    class Meta:
        model = TournamentDefinition
        exclude = []


class TournamentDefinitionAdmin(admin.ModelAdmin):
    form = TournamentDefinitionAdminForm
    list_display = ['name', 'created', 'last_updated', 'players']
    readonly_fields = ['name', 'created', 'last_updated', 'players']

admin.site.register(TournamentDefinition, TournamentDefinitionAdmin)


