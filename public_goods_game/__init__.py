from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'public_goods_game'
    players_per_group = 2
    num_rounds = 1
    endowment = cu(80)
    multiplier = 1.6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="现在轮到你决策了，你将往公共池中存入？（0-80元中任意整数）"
    )


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * Constants.multiplier / Constants.players_per_group
    )
    for p in players:
        p.payoff = Constants.endowment - p.contribution + group.individual_share


# PAGES
class Introduction(Page):
    pass

class Test(Page):
    pass

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Introduction, Test, Contribute, ResultsWaitPage, Results]
