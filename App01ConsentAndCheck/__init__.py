from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'App01ConsentAndCheck'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    ProlificId = models.StringField(label='Prolific ID')


class Group(BaseGroup):
    pass


def wait_for_all(group: Group):
    pass


def group_by_arrival_time_method(subsession, waiting_players):
    print('in group_by_arrival_time_method')
    players_consent = [p for p in waiting_players if
                       p.participant.vars['consent'] == 1 and
                       p.participant.vars['micAndCameraCheck'] == 0
                       and p.participant.vars['numberVideo'] == 2 and p.participant.vars['colorVideo'] == 3]
    print(len(players_consent))

    # todo change logic here for groups greater than 4. empty the list each time.
    if len(players_consent) >= 4:
        print('about to create a group')
        return [players_consent[0], players_consent[1], players_consent[2], players_consent[3]]
    print('not enough players yet to create a group')


class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        # save each participant's current group ID so it can be
        # accessed in the next app.
        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id


class EnterProlificId(Page):
    form_model = 'player'
    form_fields = ['ProlificId']


class PartsRoundsGroups(Page):
    form_model = 'player'


page_sequence = [MyWaitPage, EnterProlificId, PartsRoundsGroups]
