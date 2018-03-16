from django.shortcuts import render
from django.views.generic import TemplateView

# Views to register a new user
class GroupsView(TemplateView):
    template_name = 'world_cup/groups_phase.html'

    def post(self, request, *args, **kwargs):
        dict_gamble_user = {}
        for key, value in request.POST.items():
            if len(key.split("_")) == 3:
                match_id, team_number = key.split("_")
                print(match_id, team_number, value)

class SummaryView(TemplateView):
    template_name = 'world_cup/summary.html'
