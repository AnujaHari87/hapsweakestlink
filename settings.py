from os import environ

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='weakestlinkdemo', num_demo_participants=20,
                        app_sequence=['App00ConsentAndCheck', 'App01ConsentAndCheck', 'App02PostIntro',
                                      'App03WeakestLink', 'App04Questionnaires', 'App05Payoff', 'App06ThankYou',
                                      'App07ConsentThankYou'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['optInConsent', 'consent', 'micAndCameraCheck', 'numberVideo', 'colorVideo','payoff_ppg', 'payoff_round']
SESSION_FIELDS = []
ROOMS = [
    dict(
        name='HapsPilot',
        display_name='HAPS Pilot'
    )]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
