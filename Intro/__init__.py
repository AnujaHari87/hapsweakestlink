
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
def continue_function(group: Group):
    for player in group.get_players():
        player.payoff = 0
    
    
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
    personalGoal = models.LongStringField(label='List down a personal goal you would like to achieve in the game.')
    outcomeTeam = models.LongStringField(label='List down at least one outcome for the team, as a result of your goal.')
    obstacleTeam = models.LongStringField(label='List down at least one obstacle you may face in achieving this goal from any team members.')
    planTeam = models.LongStringField(label='Plan a negotiation strategy with your team member(s) for the obstacle(s) above.')
class EnterProlificId(Page):
    form_model = 'player'
    form_fields = ['ProlificId']
class AudioVideoCheck(Page):
    form_model = 'player'
class WelcomeScreen(Page):
    form_model = 'player'
class StudyIntroduction1(Page):
    form_model = 'player'
class StudyIntroduction2(Page):
    form_model = 'player'
    form_fields = ['personalGoal', 'outcomeTeam', 'obstacleTeam', 'planTeam']
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
        if (player.overallScore>= 2):
          return upcoming_apps[0]
        else:
          return upcoming_apps[-1]
page_sequence = [EnterProlificId, AudioVideoCheck, WelcomeScreen, StudyIntroduction1, StudyIntroduction2, ControlQuestion1, ControlQuestion2, ControlQuestion3]