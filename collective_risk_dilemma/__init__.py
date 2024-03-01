from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page, WaitPage,
    Currency as c, currency_range
)
import json


class Constants(BaseConstants):
    name_in_url = 'collective_risk_dilemma'
    players_per_group = 2
    num_rounds = 10
    initial_chips = 40
    chips_per_round = 4
    collective_target = 120
    success_probability_default = 90


class Subsession(BaseSubsession):

    def creating_session(subsession):
        subsession.group_randomly(fixed_id_in_group=True)



class Group(BaseGroup):
    total_climate_account = models.IntegerField(initial=0)

    def set_payoffs(self):
        # Implement logic to determine if collective target is met
        # and apply results based on the success probability treatment.
        pass


class Player(BasePlayer):
    investment = models.IntegerField(
        choices=[0,2,4], widget=widgets.RadioSelect,label="往气候账户投入的筹码数：(0，2，4中任意整数)"
    )
    private_account = models.IntegerField(initial=Constants.initial_chips)
    climate_account_contribution = models.IntegerField(initial=0)
    investments_history = models.LongStringField(initial='')

    def add_investment(player, investment):
        if player.investments_history:
            investments = json.loads(player.investments_history)
        else:
            investments = []
        investments.append(investment)
        player.investments_history = json.dumps(investments)


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.investment for p in players]
    group.total_climate_account = sum(contributions)
    for p in players:
        p.payoff = Constants.chips_per_round - p.investment 



# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Test(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1



class Contribute(Page):
    form_model = 'player'
    form_fields = ['investment']

    @staticmethod
    def before_next_page(player,timeout_happened):
        group = player.group
        player.private_account -= player.investment
        player.climate_account_contribution += player.investment
        group.total_climate_account += player.investment
        player.add_investment(player.investment)

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        # 获取当前小组的所有玩家
        group = group = player.group
        players = group.get_players()
        
        contributions = [(p.id_in_group, p.investment) for p in players]
        total_contribution = sum([p.investment for p in players])
       
        rounds = list(range(1, Constants.num_rounds + 1))
        investments_data = []
        for p in group.get_players():
            investments = json.loads(p.investments_history)
            investments_data.append({
            'label': p.id_in_group,
            'investments': investments
            })
        return {
            'rounds': rounds,
            'contributions': contributions,
            'total_contribution': total_contribution,
            'private_account': player.private_account,
            'climate_account_contribution': player.climate_account_contribution,
            'investments_data': investments_data
        }


#page_sequence = [Introduction, Test, Contribute, ResultsWaitPage, Results]

page_sequence = [Contribute, ResultsWaitPage, Results]