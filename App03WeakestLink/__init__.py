from otree.api import *
import random

c = cu

doc = ''


def make_field(label):
    return models.IntegerField(
        choices=[0, 10, 20, 30, 40],
        label=label,
        widget=widgets.RadioSelect,
    )


class C(BaseConstants):
    NAME_IN_URL = 'App03WeakestLink'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    ENDOWMENT = 200


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_like_round(1)


class Group(BaseGroup):
    groupMin = models.IntegerField(
        min=0, max=40, initial=40
    )

    randomNumber = models.IntegerField()


class Player(BasePlayer):
    ownDecision = make_field("Please choose one")
    payoff_hypo = models.IntegerField()


class Instructions1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instructions2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instructions3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Decision(Page):
    form_model = 'player'
    form_fields = ['ownDecision']

    @staticmethod
    def live_method(player: Player, data):
        if "ownDecision" in data:
            player.ownDecision = data["ownDecision"]
            group = player.group
            if player.ownDecision < group.groupMin:
                group.groupMin = player.ownDecision

    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_num=player.round_number)


class CalculatePayoff(WaitPage):
    body_text = "Please wait until your team members have made their decision."
    group_id = models.IntegerField()

    @staticmethod
    def after_all_players_arrive(group: Group):
        for p in group.get_players():
            p.payoff_hypo = C.ENDOWMENT + (6 * group.groupMin) - (5 * p.ownDecision)
        if group.round_number == 5:
            print('we are getting here')
            group.randomNumber = random.choice(range(1, 6))
            for p in group.get_players():
                p_past = p.in_round(group.randomNumber)
                g_past = group.in_round(group.randomNumber)
                p.payoff = C.ENDOWMENT + (6 * g_past.groupMin) - (5 * p_past.ownDecision)
                part = p.participant
                part.payoff_ppg = p.payoff
                part.payoff_round = group.randomNumber


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            groupMin=player.group.groupMin,
            payoff=player.payoff_hypo,
            endowment=C.ENDOWMENT,
            ownDecision=player.ownDecision,
            round_num=player.round_number
        )


page_sequence = [Decision, CalculatePayoff, Results]
