from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'App04Questionnaires'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field2(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field3(label):
    return models.IntegerField(
        choices=[0, 5, 10, 15, 20, 25, 30],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field4(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_image_data(image_names):
    return [dict(name=name, path='images/{}'.format(name)) for name in image_names]


class Player(BasePlayer):
    team_cohesion = models.StringField()
    payoff_quests = models.IntegerField()
    attention_check = models.IntegerField(initial=0)
    social_cohesion_short = make_field7('')
    risk = make_field2('')
    time_1 = make_field2(
        'How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?')

    negative_rp_1 = make_field2(
        'How willing are you to punish someone who treats you unfairly, even if there may be costs for you?')
    negative_rp_2 = make_field2(
        'How willing are you to punish someone who treats others unfairly,even if there may be costs for you?')
    altruism_1 = make_field2(
        'How willing are you to give to good causes without expecting anything in return?')
    attention2 = make_field2('Please select the option "7" to show that you are answering the questions attentively.')
    attention1 = make_field('Please select the option "1" to show that you are answering the questions attentively.')

    positive_rp_1 = make_field2('When someone does me a favor, I am willing to return it.')
    negative_rp_3 = make_field2(
        'If I am treated very unjustly, I will take revenge at the first occasion, even if there is a cost to do so.')
    trust_1_positive = make_field2('I assume that people have only the best intentions.')
    trust_2_negative = make_field2("You can't rely on anyone nowadays.")
    trust_3_positive = make_field2('In general, people can be trusted.')
    math = make_field2('I am good at math.')
    time_2 = make_field2('I tend to postpone tasks even if I know it would be better to do them right away.')
    attention3 = make_field2('Please select the option "3" to show that you are answering the questions attentively.')
    positive_rp_2 = make_field3("")
    altruism_2 = models.IntegerField(label="", min=0, max=1000)
    collective_orientation_1_p = make_field("I find working on team projects very satisfying.")
    collective_orientation_2_n = make_field(
        "I would rather take action on my own than to wait around for others' input.")
    collective_orientation_3_n = make_field(
        "I prefer to complete a task from beginning to end with no assistance from others.")
    collective_orientation_4_p = make_field("Teams usually work very effectively.")
    collective_orientation_5_n = make_field(
        "I think it is usually better to take the bull by the horns and do something yourself, rather than to wait for input from others.")
    collective_orientation_6_n = make_field("For most tasks, I would rather work alone than as part of a group.")
    collective_orientation_7_n = make_field(
        "I find it easy to negotiate with others who hold a different viewpoint than I hold.")
    collective_orientation_8_n = make_field("I can usually perform better when I work on my own.")
    collective_orientation_9_n = make_field(
        "I always ask for more information from others before making any important decision.")
    collective_orientation_10_n = make_field(
        "I find that it is often more productive to work on my own than with others.")
    collective_orientation_11_n = make_field(
        "When solving a problem, it is very important to make your own decision and stick by it.")
    collective_orientation_12_n = make_field(
        "If I disagree with other team members, I tend to go with my own gut feelings.")
    collective_orientation_13_n = make_field(
        "When I have a different opinion than another team member, I usually stick to my own opinion.")
    collective_orientation_14_n = make_field(
        "It is important to stick to your own decisions, even when others around you are trying to get you to change.")
    collective_orientation_15_n = make_field(
        "When others disagree, it is important to hold one's own ground and not give in.")
    attention4 = make_field(
        'Please select the option "strongly agree" to show that you are answering the questions attentively.')
    psychological_safety_1 = make_field('I was not afraid to be myself during the video meeting.')
    psychological_safety_2 = make_field('I was afraid to express my opinion in the meeting.')
    psychological_safety_3 = make_field('There was a threatening atmosphere in the meeting.')
    psychological_availability_1 = make_field(
        'I am confident that I was able to manage competing demands in a meeting.')
    psychological_availability_2 = make_field(
        'I am confident that I was able to deal with problems that arise in the meeting.')
    psychological_availability_3 = make_field(
        'I am confident that I was able to think clearly in the meeting.')
    psychological_availability_4 = make_field(
        'I am confident that I was able to show the right emotions in the meeting.')
    psychological_availability_5 = make_field(
        'I am confident that I was able to cope with the physical demands of the meeting.')

    big5_1 = make_field(
        'I see myself as someone who is reserved.')
    big5_2 = make_field(
        'I see myself as someone who is generally trusting.')
    big5_3 = make_field(
        'I see myself as someone who tends to be lazy.')
    big5_4 = make_field(
        'I see myself as someone who is relaxed, handles stress well.')
    big5_5 = make_field(
        'I see myself as someone who has few artistic interests.')
    big5_6 = make_field(
        'I see myself as someone who is outgoing, sociable.')
    big5_7 = make_field(
        'I see myself as someone who tends to find fault with others.')
    big5_8 = make_field(
        'I see myself as someone who does a thorough job.')
    big5_9 = make_field(
        'I see myself as someone who gets nervous easily.')
    big5_10 = make_field(
        'I see myself as someone who has an active imagination.')

    engagement_1 = make_field(
        'The video meeting was so absorbing that I forgot about everything else.')
    engagement_2 = make_field('I often thought about other things during the video meeting. ')
    engagement_3 = make_field('I was rarely distracted in the video meeting.')
    engagement_4 = make_field('Time passed quickly in the video meeting.')
    engagement_5 = make_field('I really put my heart into the video meeting.')
    engagement_6 = make_field('I got excited when actively contributing in the video meeting.')
    engagement_7 = make_field('I often felt emotionally detached from the video meeting.')
    engagement_8 = make_field('My own feelings were affected by how much I contributed in the video meeting.')
    engagement_9 = make_field('I exerted a lot of energy in the video meeting.')
    engagement_10 = make_field('I avoided actively contributing in the video meeting.')

    age = models.IntegerField(label='What is your <strong>age</strong> (years) ?', min=18, max=66)
    gender = models.IntegerField(label='<br>Which <strong>gender</strong> do you identify with?',
                                 choices=[[1, 'male'], [2, 'female'], [3, 'transgender'], [4, 'non-binary'],
                                          [5, 'prefer not to say']])
    ethnicity = models.IntegerField(
        label="<br>Which of the following <b>ethnicities</b> best describes you?<br/>",
        choices=[[1, 'Asian or Pacific Islander'], [2, 'Black or African American'], [3, 'Hispanic or Latino'],
                 [4, 'Native American or Alaskan Native'], [5, 'White or Caucasian'], [6, 'Multiracial or Biracial'],
                 [7, 'A race/ethnicity not listed here']])
    familiarity = models.IntegerField(
        label="<br>Please indicate whether you have ever <b>met a member of your team before </b> participating in this study</strong>.",
        choices=[[1, 'No, never met before'], [2, 'Yes, met in passing'],
                 [3, 'Yes, we are acquaintances']])

    education = models.IntegerField(
        label="<br>What is the highest level of <b>education</b> you have completed?</br>",
        choices=[[1, 'less than High School'], [2, 'High School/GED'], [3, 'Some College'],
                 [4, '2-year College degree'], [5, '4-year College degree'],
                 [6, 'Master’s degree'], [7, 'Doctoral degree or Professional Degree (JD, MD)']])
    prolifichours_month = models.IntegerField(
        label="<br>How many days per month do you typically use Prolific?</br>", min=0, max=31)
    prolifichours_day = models.IntegerField(
        label="<br>On the days when you use Prolific, how many hours do you typically spend on it?</br>", min=1, max=24)
    prolificprimary_income = models.IntegerField(label="Is Prolific your primary source of income?", blank=True,
                                                 choices=[[1, 'Yes'], [2, 'No'], [3, 'Other, please specify']])
    random = models.CurrencyField()
    other_income_specify = models.StringField(
        blank=True,
        label="Other"
    )


# PAGES

class IntroPart3(Page):
    form_model = 'player'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group_matrix_comm = player.session.vars.get('group_matrix')
        player.in_round(1).group.subsession.set_group_matrix(group_matrix_comm)


class Quest01(Page):
    form_model = 'player'
    form_fields = ['team_cohesion']

    def vars_for_template(self: Player):
        image_names = [
            'Picture1.png',
            'Picture2.png',
            'Picture3.png',
            'Picture4.png',
            'Picture5.png',
            'Picture6.png',
            'Picture7.png'
        ]
        return dict(image_data=make_image_data(image_names))


class Quest02(Page):
    form_model = 'player'
    form_fields = ['social_cohesion_short']
    # usability, satisfaction, intention to use


class Quest03(Page):
    form_model = 'player'
    form_fields = ['risk']


class Quest04(Page):
    form_model = 'player'
    form_fields = ['time_1', 'negative_rp_1', 'negative_rp_2', 'attention2', 'altruism_1']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention2 != 7:
            player.attention_check += 1


class Quest05(Page):
    form_model = 'player'
    form_fields = ['positive_rp_1', 'negative_rp_3', 'trust_1_positive', 'attention3', 'math', 'time_2']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention3 != 3:
            player.attention_check += 1


class Quest06(Page):
    form_model = 'player'
    form_fields = ['positive_rp_2']


class Quest07(Page):
    form_model = 'player'
    form_fields = ['altruism_2']


class Quest07a(Page):
    form_model = 'player'
    form_fields = ['big5_1', 'big5_2', 'big5_3', 'big5_4', 'big5_5',
                   'big5_6', 'big5_7', 'big5_8', 'big5_9', 'big5_10', 'attention1']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention1 != 1:
            player.attention_check += 1


class Quest08(Page):
    form_model = 'player'

    # usability, satisfaction, intention to use
    @staticmethod
    def get_form_fields(player):
        import random
        collective = ['collective_orientation_1_p', 'collective_orientation_2_n', 'collective_orientation_3_n',
                      'collective_orientation_4_p', "collective_orientation_5_n", "collective_orientation_6_n",
                      "collective_orientation_7_n", "collective_orientation_8_n", "collective_orientation_9_n",
                      'collective_orientation_10_n', 'collective_orientation_11_n', 'collective_orientation_12_n',
                      'collective_orientation_13_n', 'collective_orientation_14_n', 'collective_orientation_15_n',
                      'attention4']
        random.shuffle(collective)
        return collective

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention4 != 5:
            player.attention_check += 1


class Quest09(Page):
    form_model = 'player'


class QuestDemographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'ethnicity', 'prolifichours_month',
                   'prolifichours_day', 'prolificprimary_income', 'other_income_specify', 'familiarity']


class QuestAR(Page):
    form_model = 'player'
    form_fields = ['attractivenessrating']

    @staticmethod
    def vars_for_template(player: Player):
        image_names = [
            'teamco1.png',
            'teamco2.png',
            'teamco3.png',
            'teamco4.png',
            'teamco5.png',
            'teamco6.png',

        ]
        return dict(image_data=make_image_data(image_names))


class Quest10(Page):
    form_model = 'player'
    form_fields = ['psychological_safety_1', 'psychological_safety_2', 'psychological_safety_3',
                   'psychological_availability_1', 'psychological_availability_2', 'psychological_availability_3',
                   'psychological_availability_4', 'psychological_availability_5']


class Quest11(Page):
    form_model = 'player'
    form_fields = ['engagement_1', 'engagement_2', 'engagement_3', 'engagement_4', 'engagement_5', 'engagement_6',
                   'engagement_7', 'engagement_8', 'engagement_9', 'engagement_10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention_check <= 1:
            player.payoff_quests = 100
        else:
            player.payoff_quests = 0


class QuestEnd(Page):

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

        return dict(
            total_payoff_ecu=(200 + participant.payoff_ppg),
            total_payoff=(200 + participant.payoff_ppg) * 0.03
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [IntroPart3, Quest01, Quest02, Quest03, Quest04, Quest05, Quest06, Quest07, Quest07a, Quest08, Quest10,
                 Quest11, QuestDemographics, QuestEnd]
