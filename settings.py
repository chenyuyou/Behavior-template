from os import environ
import random

a = ['even-chance_gain','longshot_gain','even-chance_loss','longshot_loss','gain_ambiguity','loss_ambiguity','temporal_discounting','dictator_game','ultimatum_game','sequential_prisoners_dilemma','public_goods_game']
random.shuffle(a)

b= ['seat']+a+['questionnaire', 'payment_info']
SESSION_CONFIGS = [
    dict(
        name='new_experiments',
        display_name="new experiments",
        app_sequence=['questionnaire', 'payment_info'],
#        app_sequence=['even-chance_loss'],
#        app_sequence=b,
#        app_sequence=['even-chance_gain','longshot_gain','even-chance_loss','longshot_loss','gain_ambiguity','loss_ambiguity','temporal_discounting','dictator_game','ultimatum_game','sequential_prisoners_dilemma','public_goods_game','questionnaire', 'payment_info'],
        num_demo_participants=2,
    ),
#    dict(
#        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
#    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

OTREE_AUTH_LEVEL = "STUDY"



# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
#USE_POINTS = False
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']
