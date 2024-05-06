
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Payoff'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class PayoffInformation(Page):
    form_model = 'player'
class PostGameQuestionnaire(Page):
    form_model = 'player'
class ProlificPayoff(Page):
    form_model = 'player'
class ThankYou(Page):
    form_model = 'player'
page_sequence = [PayoffInformation, ProlificPayoff, ThankYou]
