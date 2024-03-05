from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page, WaitPage,
    Currency as c, currency_range
)
import json
import random

def set_payoffs(group):
    if group. total_climate_account >= Constants.collective_target:
        # 如果达到目标，每个人都保留剩余的筹码
        for p in group.get_players():
            p.payoff = p.remaining_chips
    else:
        # 如果未达到目标，根据概率决定是否失去所有筹码
        dice_roll = random.random()  # 得到一个0到1之间的随机数
        probability_of_loss = Constants.success_probability_default # 根据实验条件调整
        if dice_roll < probability_of_loss:
            for p in group.get_players():
                p.payoff = 0
        else:
            for p in group.get_players():
                p.payoff = p.remaining_chips


class Constants(BaseConstants):
    name_in_url = 'collective_risk_dilemma'
    players_per_group = 2
    num_rounds = 1
    initial_chips = 40
    chips_per_round = 4
    collective_target = int(chips_per_round/2 * players_per_group * num_rounds)
    success_probability_default = 0.5   ##  还可能是0.5和0.1
    probability = int(success_probability_default * 100)

class Subsession(BaseSubsession):
    pass

def creating_session(subsession:Subsession):
    if subsession.round_number == 1:
        players = subsession.get_players()
        random.shuffle(players)  # Shuffle to ensure randomness
            # Split players into two groups, A and B
        group_a = players[:int(Constants.players_per_group/2)]
        group_b = players[int(Constants.players_per_group/2):]
            # Assign groups
        for p in group_a:
            p.participant.vars['group'] = 'A'
        for p in group_b:
            p.participant.vars['group'] = 'B'
        # In subsequent rounds, maintain the group assignments
    else:
        for p in subsession.get_players():
            p.group = p.in_round(1).group

class Group(BaseGroup):
    total_climate_account = models.IntegerField(initial=0)

    def set_payoffs(self):
        # Implement logic to determine if collective target is met
        # and apply results based on the success probability treatment.
        pass

    def get_all_players_investment_history(self):
        investment_history = []
        players = self.get_players()
        for p in players:
            player_investment = []
            # 获取每个玩家在所有轮次的投资数据
            for player in p.in_all_rounds():
                player_investment.append(player.investment)
            investment_history.append(player_investment)
        return investment_history


class Player(BasePlayer):
    investment = models.IntegerField(
        choices=[0,2,4], widget=widgets.RadioSelect,label="往气候账户投入的筹码数：(0，2，4中任意整数)"
    )
    private_account = models.IntegerField(initial=Constants.initial_chips)
    climate_account_contribution = models.IntegerField(initial=0)
    final_payoff = models.CurrencyField()
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
        if player.round_number > 1:
            previous_player = player.in_round(player.round_number - 1)
            player.private_account = previous_player.private_account
            player.climate_account_contribution = previous_player.climate_account_contribution
        player.private_account -= player.investment
        player.climate_account_contribution += player.investment

    @staticmethod
    def is_displayed(player):
        if player.participant.vars['group'] == 'A':
            return True  # Computer makes decision
        elif player.round_number > 3 and player.participant.vars['group'] == 'B':
            return True  # Player makes decision
        
class Contribute_by_Computer(Page):
    @staticmethod
    def before_next_page(player,timeout_happened):
        player.investment = Constants.chips_per_round
        if player.round_number > 1:
            previous_player = player.in_round(player.round_number - 1)
            player.private_account = previous_player.private_account
            player.climate_account_contribution = previous_player.climate_account_contribution
        player.private_account -= player.investment
        player.climate_account_contribution += player.investment

    @staticmethod
    def is_displayed(player):
        if player.round_number <= 3 and player.participant.vars['group'] == 'B':
            return True  # Player makes decision


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        total_investment = sum([p.investment for p in group.get_players()])
        if group.round_number > 1:
            previous_group = group.in_round(group.round_number - 1)
            group.total_climate_account = previous_group.total_climate_account 
        group.total_climate_account += total_investment


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        # 获取当前小组的所有玩家
        group = group = player.group
        players = group.get_players()      
        contributions = [(p.id_in_group, p.investment) for p in players]
        total_contribution = sum([p.investment for p in players])    
        rounds = list(range(1, Constants.num_rounds + 1))
        investment_history = group.get_all_players_investment_history()
        return {
            'rounds': rounds,
            'contributions': contributions,
            'total_contribution': total_contribution,
            'private_account': player.private_account,
            'climate_account_contribution': player.climate_account_contribution,
            'investment_history': investment_history,
            'num_rounds': Constants.num_rounds
        }

class ResultsFinal(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player):
        group = player.group
        success = group.total_climate_account >= Constants.collective_target
        for p in group.get_players():
            if success:
                p.final_payoff = p.private_account
            else:
                if random.random()>Constants.success_probability_default:
                    p.final_payoff = 0  # 或者任何未成功时的收益逻辑
                else:
                    p.final_payoff = p.private_account
            p.payoff = p.final_payoff
        return {
            'success': success,
            'final_payoff': player.final_payoff,
            'total_investment': group.total_climate_account
        }


#page_sequence = [Introduction, Test, Contribute, ResultsWaitPage, Results, ResultsFinal]

page_sequence = [Contribute,Contribute_by_Computer, ResultsWaitPage, Results, ResultsFinal]
