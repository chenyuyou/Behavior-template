from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'ultimatum_game/instructions.html'
    # Initial amount allocated to the dictator
    endowment = cu(120)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    offer = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment,
        label="我打算给参与者B",
    )

    accept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment,
        label="最少我能接受多少？",
    )

class Player(BasePlayer):
    pass


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if group.accept <= group.offer:
        p1.payoff = Constants.endowment - group.offer
        p2.payoff = group.offer
    else:
        p1.payoff = 0
        p2.payoff = 0


# PAGES
class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['offer']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class Accept(Page):
    form_model = 'group'
    form_fields = ['accept']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        


page_sequence = [Introduction, Offer, Accept, ResultsWaitPage, Results]
