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


def make_field2(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field3(label):
    return models.IntegerField(
        choices=[5, 10, 15, 20, 25, 30],
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
    payoff_quests = models.IntegerField()

    attention_check = models.IntegerField(initial=0)
    team_cohesion = models.StringField()

    social_cohesion_1 = make_field('I felt accepted by my team members.')
    social_cohesion_2 = make_field('I could trust my team members.')
    social_cohesion_3 = make_field('The members of my team liked each other.')
    social_cohesion_4 = make_field('The members of my team made an effort to understand the opinions of others.')
    social_cohesion_5 = make_field(
        'The members of my team seemed to make an effort to behave in a way that is acceptable to others.')
    social_cohesion_6 = make_field('The members of my team disclosed personal information or feelings.')
    attention1 = make_field(
        'Please select the option "strongly disagree" to show that you are answering the questions attentively.')

    risk = make_field2('Are you generally a risk-taking person or do you try to avoid risks?')

    time_1 = make_field2(
        'How much would you be willing to give up on something that benefits you today in order to benefit more in the future?')
    negative_rp_1 = make_field2(
        'How much would you be willing to punish someone who treated YOU unfairly, even if this would have negative consequences for you?')
    negative_rp_2 = make_field2(
        'How much would you be willing to punish someone who treated OTHERS unfairly, even if this would incur costs for you?')
    altruism_1 = make_field2(
        'How much would you be willing to give for a good cause, without expecting anything in return?')
    attention2 = make_field2('Please select the option "7" to show that you are answering the questions attentively.')

    positive_rp_1 = make_field2('If someone does me a favor, I am willing to reciprocate.')
    negative_rp_3 = make_field2(
        'If I am treated very unfairly, I will seek revenge at the first opportunity, even if it costs me to do so.')
    trust_1_positive = make_field2('I am convinced that most people have good intentions.')
    trust_2_negative = make_field2("Nowadays, you can't rely on anyone anymore.")
    trust_3_positive = make_field2('In general, people can be trusted.')
    math = make_field2('I am good at mathematics.')
    time_2 = make_field2('I tend to procrastinate tasks, even though I know it would be better to do them right away.')
    attention3 = make_field2('Please select the option "3" to show that you are answering the questions attentively.')

    positive_rp_2 = make_field3("")
    altruism_2 = models.IntegerField(label="", min=0, max=1000)

    collective_orientation_1_p = make_field("I find working on team projects very satisfying.")
    collective_orientation_2_n = make_field("I would rather act on my own than wait for input from others.")
    collective_orientation_3_n = make_field(
        "I prefer to complete a task from start to finish without the support of others.")
    collective_orientation_4_p = make_field("Teams usually work very effectively.")
    collective_orientation_5_n = make_field(
        "I think it is usually better to take the bull by the horns and do something myself than to wait for input from others.")
    collective_orientation_6_n = make_field("For most tasks, I would rather work alone than be part of a group.")
    collective_orientation_7_n = make_field("I can usually achieve more when I work alone.")
    collective_orientation_8_n = make_field("I think it is generally more productive to work alone than with others.")
    collective_orientation_9_p = make_field("I enjoy working with others.")
    collective_orientation_10_n = make_field("I do not like having to rely on other team members.")
    collective_orientation_11_n = make_field(
        "If I disagree with other team members, I tend to follow my own gut feeling.")
    collective_orientation_12_n = make_field(
        "If I have a different opinion than another team member, I usually try to stick to my own opinion.")
    collective_orientation_13_n = make_field(
        "It is important to stick to your own opinion, especially when others around you try to persuade you to change it.")
    collective_orientation_14_n = make_field("When others disagree, it is important to stand firm and not give in.")
    collective_orientation_15_n = make_field(
        "Even in teamwork, I believe you should always do what you think is right.")
    collective_orientation_16_n = make_field(
        "If I am convinced of something, I stick to my opinion, no matter what other team members say.")
    attention4 = make_field(
        'Please select the option "strongly agree" to show that you are answering the questions attentively.')

    gaze_anxiety_1 = make_field4('Giving a speech.')
    gaze_anxiety_2 = make_field4('Talking with a group of people at a party.')
    gaze_anxiety_3 = make_field4('Taking the floor at a meeting.')
    gaze_anxiety_4 = make_field4('Speaking in a discussion with several people.')
    gaze_anxiety_5 = make_field4('Speaking with a cashier while shopping.')
    gaze_anxiety_6 = make_field4('Being introduced to someone.')
    gaze_anxiety_7 = make_field4('Greeting an acquaintance passing by on the street.')
    gaze_anxiety_8 = make_field4('Talking with someone you do not know well.')
    gaze_anxiety_9 = make_field4('Talking with someone you find attractive.')
    gaze_anxiety_10 = make_field4('Going on a date with someone you do not know well.')
    gaze_anxiety_11 = make_field4('Being in a familiar situation with someone close to you.')
    gaze_anxiety_12 = make_field4('Discussing the quality of your work with an authority figure.')
    gaze_anxiety_13 = make_field4('Having an everyday conversation with a close family member.')
    gaze_anxiety_14 = make_field4('Listening to someone talk to you.')
    gaze_anxiety_15 = make_field4('Talking with someone who is listening to you.')
    gaze_anxiety_16 = make_field4('Expressing a disagreement.')
    gaze_anxiety_17 = make_field4('Receiving a compliment.')

    psychological_safety_1 = make_field('I was not afraid to be myself during the video meeting.')
    psychological_safety_2 = make_field('I was afraid to express my opinion during the video meeting.')
    psychological_safety_3 = make_field('There was a threatening atmosphere during the video meeting.')
    psychological_availability_1 = make_field(
        'I am confident that I was able to handle competing demands during the video meeting.')
    psychological_availability_2 = make_field(
        'I am confident that I was able to deal with problems that arose during the video meeting.')
    psychological_availability_3 = make_field(
        'I am confident that I was able to think clearly during the video meeting.')
    psychological_availability_4 = make_field(
        'I am confident that I was able to show the right emotions during the video meeting.')
    psychological_availability_5 = make_field(
        'I am confident that I was able to cope with the physical demands during the video meeting.')

    engagement_1 = make_field('I was full of energy during the video meeting.')
    engagement_2 = make_field('The video meeting was useful and meaningful.')
    engagement_3 = make_field('Time flew by while I was in the video meeting.')
    engagement_4 = make_field('I felt energetic and vigorous during the video meeting.')
    engagement_5 = make_field('I was excited about the video meeting.')
    engagement_6 = make_field('I forgot everything around me while I was in the video meeting.')
    engagement_7 = make_field('The video meeting inspired me.')
    engagement_8 = make_field('When I woke up in the morning, I looked forward to the video meeting.')
    engagement_9 = make_field('I felt happy when I worked intensively during the video meeting.')
    engagement_10 = make_field('I am proud of my work in the video meeting.')
    engagement_11 = make_field('I was completely absorbed in my work in the video meeting.')
    engagement_12 = make_field('When I was in the video meeting, I could work for a very long time.')
    engagement_13 = make_field('The video meeting was a challenge for me.')
    engagement_14 = make_field('The video meeting swept me away.')
    engagement_15 = make_field('I was mentally very resilient in the video meeting.')
    engagement_16 = make_field('I found it difficult to tear myself away from the video meeting.')
    engagement_17 = make_field('I persevered in the video meeting, even when things were not going well.')
    engagement_18 = make_field(
        'The fulfillment of my task in the video meeting was so captivating that I forgot everything else.')
    engagement_19 = make_field('I often thought about other things while I was in the video meeting.')
    engagement_20 = make_field('I was rarely distracted while I was in the video meeting.')
    engagement_21 = make_field('Time passed quickly while I was in the video meeting.')
    engagement_22 = make_field('I was very committed in the video meeting.')
    engagement_23 = make_field('I was excited to do well in the video meeting.')
    engagement_24 = make_field('I often felt emotionally detached from the video meeting.')
    engagement_25 = make_field('My own feelings depended on how well I did in the video meeting.')
    engagement_26 = make_field('I expended a lot of energy to do well in the video meeting.')
    engagement_27 = make_field('I stayed in the video meeting until the work was done.')
    engagement_28 = make_field('I spent longer in the video meeting than necessary when possible.')
    engagement_29 = make_field('I took work from the video meeting home to complete it.')
    engagement_30 = make_field('I avoided working too hard in the video meeting.')

    age = models.IntegerField(label='Please enter your <strong>age</strong>.', min=18, max=100)
    gender = models.IntegerField(label='<br>Please enter your <strong>gender</strong>.',
                                 choices=[[1, 'female'], [2, 'male'], [3, 'diverse']])
    studies = models.StringField(label="<br>Please enter your <strong>current field of study</strong>.")
    ethnicity = models.IntegerField(
        label="<br>Please indicate which <strong>ethnicity</strong> you would <u>most likely</u> identify with.",
        choices=[[1, 'Asian or Pacific'], [2, 'Black or African American'], [3, 'Hispanic or Latino'],
                 [4, 'White or Caucasian']])
    economics = models.IntegerField(
        label="<br>Please indicate whether you have ever participated in an <strong>economic study</strong>.",
        choices=[[1, "Yes"], [2, "No"]])
    familiarity = models.IntegerField(
        label="<br>Please indicate whether you have <strong>encountered a member of your team before participating in this study</strong>.",
        choices=[[1, 'No, never encountered before'], [2, 'Yes, encountered casually before'],
                 [3, 'Yes, we know each other']])

    random = models.CurrencyField()
    attractiveness_rating = models.IntegerField(label='Rate the image from -5 to 5:',
                                                choices=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                                                widget=widgets.RadioSelect)


# PAGES

class Quest02(Page):
    form_model = 'player'

    # usability, satisfaction, intention to use
    @staticmethod
    def get_form_fields(player):
        import random
        soco = ['social_cohesion_1', 'social_cohesion_2', 'social_cohesion_3', 'social_cohesion_4', 'social_cohesion_5',
                'social_cohesion_6', 'attention1']
        random.shuffle(soco)
        return soco

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention1 != 1:
            player.attention_check += 1


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
    form_fields = ['positive_rp_1', 'negative_rp_3', 'trust_1_positive', 'trust_2_negative', 'trust_3_positive',
                   'attention3', 'math', 'time_2']

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


class Quest08(Page):
    form_model = 'player'

    # usability, satisfaction, intention to use
    @staticmethod
    def get_form_fields(player):
        import random
        collective = ['collective_orientation_1_p', 'collective_orientation_2_n', 'collective_orientation_3_n',
                      'collective_orientation_4_p', "collective_orientation_5_n", "collective_orientation_6_n",
                      "collective_orientation_7_n", "collective_orientation_8_n", "collective_orientation_9_p",
                      'collective_orientation_10_n', 'collective_orientation_11_n', 'collective_orientation_12_n',
                      'collective_orientation_13_n', 'collective_orientation_14_n', 'collective_orientation_15_n',
                      'collective_orientation_16_n', 'attention4']
        random.shuffle(collective)
        return collective

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.attention4 != 5:
            player.attention_check += 1


class Quest09(Page):
    form_model = 'player'
    form_fields = ['gaze_anxiety_1', 'gaze_anxiety_2', 'gaze_anxiety_3', 'gaze_anxiety_4', "gaze_anxiety_5",
                   "gaze_anxiety_6", "gaze_anxiety_7", "gaze_anxiety_8", "gaze_anxiety_9", 'gaze_anxiety_10',
                   'gaze_anxiety_11', 'gaze_anxiety_12', 'gaze_anxiety_13', 'gaze_anxiety_14', 'gaze_anxiety_15',
                   'gaze_anxiety_16', 'gaze_anxiety_17']


class QuestDemographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'studies', 'ethnicity', 'economics', 'familiarity']


class QuestAR(Page):
    form_model = 'player'
    form_fields = ['attricativenessrating']

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
                   'engagement_7', 'engagement_8', 'engagement_9', 'engagement_10', 'engagement_11', 'engagement_12',
                   'engagement_13', 'engagement_14', 'engagement_15', 'engagement_16', 'engagement_17', 'engagement_18',
                   'engagement_19', 'engagement_20', 'engagement_21', 'engagement_22', 'engagement_23', 'engagement_24',
                   'engagement_25', 'engagement_26', 'engagement_27', 'engagement_28', 'engagement_29', 'engagement_30']

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
            total_payoff=(200 + player.payoff_quests) * 0.03
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Quest02, Quest03, Quest04, Quest05, Quest06, Quest07, Quest08, Quest09, Quest10, Quest11,
                 QuestDemographics, QuestEnd]
