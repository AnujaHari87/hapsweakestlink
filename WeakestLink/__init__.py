
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'WeakestLink'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
def calculateminchoice(group: Group):
    players = group.get_players()
    choices = [p.roundChoice for p in players]
    min_choice = min(choices)
    for player in players:
        player.payoff = min_choice*10
        player.minChoice = min_choice
class Player(BasePlayer):
    roundChoice = models.IntegerField(initial=1, label='Your choice:', max=7, min=1)
    minChoice = models.IntegerField(initial=0)
class WeakestLink1(Page):
    form_model = 'player'
    form_fields = ['roundChoice']
class WaitingScreen(WaitPage):
    after_all_players_arrive = calculateminchoice
    title_text = 'Weakest Link (Waiting screen)'
    body_text = 'Your choice has been reported.\u200b  Please wait until the other two participants have reported their choice.'
class Resultpage(Page):
    form_model = 'group'
page_sequence = [WeakestLink1, WaitingScreen, Resultpage]