from otree.api import *
from random import choice


doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'dictator_game/instructions.html'
    # Initial amount allocated to the dictator
    endowment160_1 = cu(160)
    endowment80 = cu(80)
    endowment160_2 = cu(160)
    endowment240 = cu(240)
    endowment120 = cu(120)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    kept160_1 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment160_1,
        label="",
    )
    kept80 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment80,
        label="我保留",
    )
    kept160_2 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment160_2,
        label="我保留",
    )
    kept240 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment240,
        label="我保留",
    )
    kept120 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment120,
        label="我保留",
    )

    send160_1 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment160_1,
        label="",
    )
    send80 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment80,
        label="我给出",
    )
    send160_2 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment160_2,
        label="我给出",
    )
    send240 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment240,
        label="我给出",
    )
    send120 = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment120,
        label="我给出",
    )


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = choice([Constants.endowment160_1 - p1.kept160_1, Constants.endowment80 - p1.kept80, Constants.endowment160_2 - p1.kept160_2, Constants.endowment240 - p1.kept240, Constants.endowment120 - p1.kept120])
    p2.payoff = choice([Constants.endowment160_1 - p2.kept160_1, Constants.endowment80 - p2.kept80, Constants.endowment160_2 - p2.kept160_2, Constants.endowment240 - p2.kept240, Constants.endowment120 - p2.kept120])


# PAGES
class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'player'
    form_fields = ['kept160_1', 'kept80', 'kept160_2', 'kept240', 'kept120', 'send160_1', 'send80', 'send160_2', 'send240', 'send120',]





class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        

        return dict(offer= player.kept80)


page_sequence = [Introduction, Offer, ResultsWaitPage, Results]
