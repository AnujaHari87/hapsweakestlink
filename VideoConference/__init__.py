
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'VideoConference'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
def wait_for_all(group: Group):
    pass
class Player(BasePlayer):
    consentAudio = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], initial=False, label='I agree to share my video for the duration of this experiment')
    consentVideo = models.BooleanField(initial=False, label='I agree to share my video for the duration of this experiment')
class Consentform(Page):
    form_model = 'player'
    form_fields = ['consentAudio', 'consentVideo']
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if (not player.consentAudio) or (not player.consentVideo):
          return upcoming_apps[-1]
class WaitConsent(WaitPage):
    after_all_players_arrive = wait_for_all
    title_text = 'Please wait...'
    body_text = 'You have now been matched with two other participants and will meet them in a Jitsi video meeting. \u200b  The meeting will last for 5 minutes and will then be terminated automatically. Remember that you will afterwards play the game with the same two participants. Your meeting time starts as soon as you are joined by the other two participants.\u200b'
class VVC(Page):
    form_model = 'group'
    timeout_seconds = 60
    @staticmethod
    def is_displayed(player: Player):
        return player.consentAudio & player.consentVideo
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]
class EndVVC(Page):
    form_model = 'player'
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]
page_sequence = [Consentform, WaitConsent, VVC, EndVVC]