from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'App01ConsentAndCheck'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        consents = [p for p in self.get_players() if p.participant.vars['consent'] == 1 and
                    p.participant.vars['micAndCameraCheck'] == 0
                    and p.participant.vars['numberVideo'] == 2 and p.participant.vars['colorVideo'] == 3]
        self.set_group_matrix([consents[i:i + 4] for i in range(0, len(consents), 4)])


class Player(BasePlayer):
    ProlificId = models.StringField(label='Prolific ID')


class Group(BaseGroup):
    pass


def wait_for_all(group: Group):
    pass


class EnterProlificId(Page):
    form_model = 'player'
    form_fields = ['ProlificId']


class PartsRoundsGroups(Page):
    form_model = 'player'


page_sequence = [EnterProlificId, PartsRoundsGroups]
