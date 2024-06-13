from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = '02_Post_Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def wait_for_all(group: Group):
    pass


def goal_wait_for_all(group: Group):
    pass


def make_image_data(image_names):
    return [dict(name=name, path='images/{}'.format(name)) for name in image_names]


def make_field(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    holidays_1 = make_field('Sun, sea, and beach holiday.')
    holidays_2 = make_field('Party holiday.')
    holidays_3 = make_field('Winter sports holiday.')
    holidays_4 = make_field('City trip.')
    holidays_5 = make_field('Backpacking holiday.')
    holidays_6 = make_field('Excursion.')
    holidays_7 = make_field('Camping holiday.')
    holidays_8 = make_field('Cruise holiday.')
    comp1_check = models.IntegerField(initial=0)
    comp2_check = models.IntegerField(initial=0)
    comp3_check = models.IntegerField(initial=0)
    comp4_check = models.IntegerField(initial=0)
    comprehension1 = models.IntegerField(
        label='<br><strong>What would be your compensation if you work 0 hours on Project A '
              'and the lowest contribution of a team member to Project A is 10 hours?</strong>', min=0, max=240)
    comprehension2 = models.IntegerField(
        label='<br><strong>What would be your compensation if you work 20 hours on Project A '
              'and the lowest contribution of a team member to Project A is 10 hours?</strong>', min=0, max=240)
    comprehension3 = models.IntegerField(
        label='<br><strong>What would be your compensation if you work 40 hours on Project A '
              'and the lowest contribution of a team member to Project A is 30 hours?</strong>', min=0, max=240)

    comprehension4a = models.BooleanField(
        default=False,
        label='',
        widget=widgets.CheckboxInput,
        blank=True
    )
    comprehension4b = models.BooleanField(
        default=False,
        label='',
        widget=widgets.CheckboxInput,
        blank=True
    )
    comprehension4c = models.BooleanField(
        default=False,
        label='',
        widget=widgets.CheckboxInput,
        blank=True
    )


def comprehension1_error_message(player: Player, value):
    if value != 200:
        player.comp1_check += 1
        if player.comp1_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        if player.comp1_check >= 2:
            return "Unfortunately, that's incorrect. The correct answer is <strong>200</strong>."
    return None  # Allow the participant to try again if they haven't clicked incorrectly twice


def comprehension2_error_message(player: Player, value):
    if value != 160:
        player.comp2_check += 1
        if player.comp2_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        elif player.comp2_check >= 2:
            return "Unfortunately, that's incorrect. The correct answer is <strong>160</strong>."
    return None


def comprehension3_error_message(player: Player, value):
    if value != 180:
        player.comp3_check += 1
        if player.comp3_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        elif player.comp3_check >= 2:
            return "Unfortunately, that's incorrect. The correct answer is <strong>180</strong>."
    return None


def comprehension4a_error_message(player: Player, value):
    if not value:
        player.comp4_check += 1
        if player.comp4_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        elif player.comp4_check >= 2:
            return "Unfortunately, that's incorrect. Your compensation depends on the <strong>number of hours you work on Project A</strong> and the <strong>fewest number of hours worked by a member of your team on Project A</strong>."
    return None


def comprehension4b_error_message(player: Player, value):
    if value:
        player.comp4_check += 1
        if player.comp4_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        elif player.comp4_check >= 2:
            return "Unfortunately, that's incorrect. Your compensation depends on the <strong>number of hours you work on Project A</strong> and the <strong>fewest number of hours worked by a member of your team on Project A</strong>."
    return None


def comprehension4c_error_message(player: Player, value):
    if not value:
        player.comp4_check += 1
        if player.comp4_check == 1:
            return "Unfortunately, that's incorrect. Please try again."
        elif player.comp4_check >= 2:
            return "Unfortunately, that's incorrect. Your compensation depends on the <strong>number of hours you work on Project A</strong> and the <strong>fewest number of hours worked by a member of your team on Project A</strong>."
    return None


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


class DescriptionVideoCommunication(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        import random
        holidays = ['holidays_1', 'holidays_2', 'holidays_3', 'holidays_4',
                    'holidays_5', 'holidays_6', 'holidays_7', 'holidays_8']
        random.shuffle(holidays)
        return holidays


class DescriptionVideoCommunication1(Page):
    form_model = 'player'


class GroupWaitPage(WaitPage):
    wait_for_all_groups = False
    body_text = 'Please wait till all players in your group have entered the test video meeting.'
    after_all_players_arrive = goal_wait_for_all


class GroupWaitPage0(WaitPage):
    group_by_arrival_time = True


class WaitBeforeVideoTest(WaitPage):
    after_all_players_arrive = goal_wait_for_all
    title_text = 'Please wait till all players have entered the test video meeting.'


class WaitBeforeVideo(WaitPage):
    after_all_players_arrive = goal_wait_for_all
    title_text = 'Please wait till all players have entered the video meeting.'


class VVC(Page):
    form_model = 'group'
    timeout_seconds = 120

    @staticmethod
    def vars_for_template(player: Player):
        optInConsent = player.participant.vars['optInConsent']
        return dict(optInConsent=optInConsent)


class VVC0(Page):
    form_model = 'group'
    timeout_seconds = 60


class EndVVC(Page):
    form_model = 'player'


class StudyIntroduction1(Page):
    form_model = 'player'


class StudyIntroduction2(Page):
    form_model = 'player'


class StudyIntroduction3(Page):
    form_model = 'player'


class StudyIntroduction4(Page):
    form_model = 'player'
    form_fields = ['comprehension1', 'comprehension2', 'comprehension3', 'comprehension4a', 'comprehension4b',
                   'comprehension4c']


class Comprehension1(Page):
    form_model = 'player'
    form_fields = ['comprehension1']


class Comprehension2(Page):
    form_model = 'player'
    form_fields = ['comprehension2']


class Comprehension3(Page):
    form_model = 'player'
    form_fields = ['comprehension3']


class Comprehension4(Page):
    form_model = 'player'
    form_fields = ['comprehension4a', 'comprehension4b', 'comprehension4c']


page_sequence = [GroupWaitPage0, DescriptionVideoCommunication, GroupWaitPage, VVC0, DescriptionVideoCommunication1,
                 WaitBeforeVideo, VVC, EndVVC, StudyIntroduction1,
                 StudyIntroduction2, StudyIntroduction3, Comprehension1, Comprehension2, Comprehension3, Comprehension4]
