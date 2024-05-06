
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'App01PreIntro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
def continue_function(group: Group):
    for player in group.get_players():
        player.payoff = 0

def wait_for_all(group: Group):
    pass
def goal_wait_for_all(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p3 = group.get_player_by_id(3)
    
    for player in group.get_players():
            player.riskAversion1 = p1.riskAversion
            player.riskAversion2 = p2.riskAversion
            player.riskAversion3 = p3.riskAversion
def make_field(label):
    return models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label=label,
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    ProlificId = models.StringField(label='Prolific ID')
    cq1mypayoff = models.IntegerField(label='My payoff (in cents):')
    cq1part2payoff = models.IntegerField(label='Payoff participant II (in cents):')
    cq1part3payoff = models.FloatField(label='Payoff participant III (in cents):')
    cq2mypayoff = models.IntegerField(label='My payoff (in cents):')
    cq2part2payoff = models.FloatField(label='Payoff participant II (in cents):')
    cq2part3payoff = models.FloatField(label='Payoff participant III (in cents):')
    cq3mypayoff = models.IntegerField(label='My payoff (in cents):')
    cq3part2payoff = models.IntegerField(label='Payoff participant II (in cents):')
    cq3part3payoff = models.IntegerField(label='Payoff participant III (in cents):')
    cq1correct = models.BooleanField(initial=False)
    cq2correct = models.BooleanField(initial=False)
    cq3correct = models.BooleanField(initial=False)
    overallScore = models.IntegerField()
    riskAversion = models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], initial=5, label='Please use a scale from 0 to 10, where a 0 means you are “completely unwilling to take risks” and a 10 means you are “very willing to take risks”.', widget=widgets.RadioSelectHorizontal)
    riskAversion1 = models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], initial=5, widget=widgets.RadioSelect)
    riskAversion2 = models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], initial=0, widget=widgets.RadioSelect)
    riskAversion3 = models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], initial=0, widget=widgets.RadioSelect)
    audioCheck = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']] , label='Audio Output', attrs={"invisible": True})
    micCheck = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']], label='Microphone Input', attrs={"invisible": True})
    cameraCheck = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']], label='Camera View', attrs={"invisible": True})
    holidays_1 = make_field('Sun, sea, and beach vacation.')
    holidays_2 = make_field('Party vacation.')
    holidays_3 = make_field('Winter sports vacation.')
    holidays_4 = make_field('City trip.')
    holidays_5 = make_field('Educational trip.')
    holidays_6 = make_field('Camping vacation.')
    holidays_7 = make_field('Cruise vacation.')

class IceBreaker(Page):
    form_model = 'player'
    # trust in peers, trust in community, social presence
    @staticmethod
    def get_form_fields(player):
        import random
        holidays = ['holidays_1', 'holidays_2', 'holidays_3', 'holidays_4',
                 'holidays_5', 'holidays_6', 'holidays_7']
        random.shuffle(holidays)
        return holidays

class EnterProlificId(Page):
    form_model = 'player'
    form_fields = ['ProlificId']
class AudioVideoCheck(Page):
    form_model = 'player'
    form_fields = ['cameraCheck', 'audioCheck', 'micCheck']
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.audioCheck == 0 or player.micCheck == 0 or player.cameraCheck == 0:
            return 'App06ThankYou'
class GeneralInformation(Page):
    form_model = 'player'
class PartsRoundsGroups(Page):
    form_model = 'player'
class WaitBeforeQuestionnaire(WaitPage):
    after_all_players_arrive = wait_for_all
    title_text = 'Please wait till other players are ready'
class PreCommunicationQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['riskAversion']
class DescriptionVideoCommunication(Page):
    form_model = 'player'
class WaitBeforeVideo(WaitPage):
    after_all_players_arrive = goal_wait_for_all
    title_text = 'Please wait till all players are ready.'

class ControlQuestion1(Page):
    form_model = 'player'
    form_fields = ['cq1mypayoff', 'cq1part2payoff', 'cq1part3payoff']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.cq1mypayoff == 70 and player.cq1part2payoff==70 and player.cq1part3payoff ==70:
            player.cq1correct=True
        else:      
            player.cq1correct=False
class ControlQuestion2(Page):
    form_model = 'player'
    form_fields = ['cq2mypayoff', 'cq2part2payoff', 'cq2part3payoff']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.cq2mypayoff == 40 and player.cq2part2payoff==40 and player.cq2part3payoff ==40:
            player.cq2correct=True
        else:      
            player.cq2correct=False
class ControlQuestion3(Page):
    form_model = 'player'
    form_fields = ['cq3mypayoff', 'cq3part2payoff', 'cq3part3payoff']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.cq3mypayoff==100 and player.cq3part2payoff==100 and player.cq3part3payoff==100:
            player.cq3correct=True
        else:      
            player.cq3correct=False  
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.overallScore = int (player.cq1correct)+ int(player.cq2correct)+ int(player.cq3correct)
page_sequence = [EnterProlificId, AudioVideoCheck, GeneralInformation, PartsRoundsGroups, IceBreaker]
