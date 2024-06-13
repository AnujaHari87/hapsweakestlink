from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'App08PreIntro_old'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def wait_for_all(group: Group):
    pass


def group_by_arrival_time_method(subsession, waiting_players):
    print('in group_by_arrival_time_method')
    players_consent = [p for p in waiting_players if p.participant.consent == '1' and
                       p.participant.micAndCameraCheck == 0
                       and p.participant.numberVideo == 2 and p.participant.colorVideo == 3]

    if len(players_consent) >= 4:
        print('about to create a group')
        return [players_consent[0], players_consent[1], players_consent[2], players_consent[3]]
    print('not enough players yet to create a group')


class Player(BasePlayer):
    ProlificId = models.StringField(label='Prolific ID')
    consent = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']], label='Consent',
                                  attrs={"invisible": True})
    optInConsent = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']], label='Opt-In Consent',
                                       attrs={"invisible": True})
    colorVideo = models.IntegerField(blank=False, label="What color was mentioned in the video?",
                                     choices=[[0, 'Red'], [1, 'Blue'], [2, 'Green'], [3, 'Yellow']])
    numberVideo = models.IntegerField(blank=False, label="Which number was shown in the video?",
                                      choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    micAndCameraCheck = models.IntegerField(blank=False, choices=[[0, 'Yes, I confirm.'], [1, 'No, I do not confirm']],
                                            label='',
                                            attrs={"invisible": True})

class EnterProlificId(Page):
    form_model = 'player'
    form_fields = ['ProlificId']


class ConsentFormA(Page):
    form_model = 'player'


class ConsentFormB(Page):
    form_model = 'player'
    form_fields = ['consent', 'optInConsent']

    def before_next_page(player: Player, timeout_happened):
        if not timeout_happened:
            player.participant.vars['optInConsent'] = player.optInConsent

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.consent == 0:
            return 'App07ConsentThankYou'


class AudioVideoCheck(Page):
    form_model = 'player'
    form_fields = ['colorVideo', 'numberVideo', 'micAndCameraCheck']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.micAndCameraCheck == 1 or player.numberVideo != 2 or player.colorVideo != 3:
            return 'App06ThankYou'


class GeneralInformation(Page):
    form_model = 'player'


class PartsRoundsGroups(Page):
    form_model = 'player'


class WaitBeforeQuestionnaire(WaitPage):
    after_all_players_arrive = wait_for_all
    title_text = 'Please wait till other players are ready'


class DescriptionInterventions(Page):
    form_model = 'player'


class Interventions(Page):
    form_model = 'player'


page_sequence = [GeneralInformation, ConsentFormA, ConsentFormB, AudioVideoCheck, EnterProlificId,
                 PartsRoundsGroups]
