
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'App05Payoff'
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

class ProlificPayoff(Page):
    form_model = 'player'
class ThankYou(Page):
    form_model = 'player'

def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    # we now place users into different baskets, according to their group in the previous app.
    # the dict 'd' will contain all these baskets.
    d = {}
    for p in waiting_players:
        group_id = p.participant.past_group_id
        if group_id not in d:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            d[group_id] = []
        players_in_my_group = d[group_id]
        players_in_my_group.append(p)
        if len(players_in_my_group) == 4:
            return players_in_my_group
        # print('d is', d)

class GroupWaitPage0(WaitPage):
   group_by_arrival_time = True

page_sequence = [GroupWaitPage0, ThankYou]
