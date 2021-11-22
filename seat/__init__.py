from otree.api import *




doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'seat'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    seat = models.StringField(label="")


# FUNCTIONS






class Seat(Page):
    form_model = 'player'
    form_fields = ['seat']





page_sequence = [Seat]
