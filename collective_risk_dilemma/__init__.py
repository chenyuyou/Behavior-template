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
    num_rounds = 10
    initial_chips = 40
    chips_per_round = 4
    collective_target = 120
    success_probability_default = 0.9


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
    investment_history = models.LongStringField(initial='')

#    def add_investment(player,investment):
#        if player.investments_history:
#            investments = json.loads(player.investments_history)
#        else:
#            investments = {}
#        investments[str(player.round_number)] = investment
#        player.investments_history = json.dumps(investments)
    def add_investment(self, round_number, investment):
        # 更新投资历史
        if not self.investment_history:
            self.investment_history = json.dumps({})

        investment_history = json.loads(self.investment_history)
        investment_history[str(round_number)] = investment
        self.investment_history = json.dumps(investment_history)




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
        if player.round_number > 1:
            previous_player = player.in_round(player.round_number - 1)
            previous_group = group.in_round(player.round_number - 1)
            player.private_account = previous_player.private_account
            player.climate_account_contribution = previous_player.climate_account_contribution
            group.total_climate_account = previous_group.total_climate_account           
        player.private_account -= player.investment
        player.climate_account_contribution += player.investment
        group.total_climate_account += player.investment
        player.add_investment(player.round_number, player.investment)


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
#        investments_data = []
#        for p in group.get_players():
#            investments = json.loads(p.investments_history)
#            investments_data.append({
#            'label': p.id_in_group,
#            'investments': investments
#            })
        # 调用Group类中的方法获取投资历史
        investments1 = [
            # 示例数据
            [2, 0, 4, 2, 4, 0, 2, 4, 2, 0],
            [4, 2, 0, 4, 2, 4, 0, 2, 4, 2],
            # 其他数据...
        ]
        # 将Python对象转换为JSON字符串
        investments_json = json.dumps(investments1)

        return {
            'rounds': rounds,
            'contributions': contributions,
            'total_contribution': total_contribution,
            'private_account': player.private_account,
            'climate_account_contribution': player.climate_account_contribution,
            'investments_json': investments_json
        }


#page_sequence = [Introduction, Test, Contribute, ResultsWaitPage, Results]

page_sequence = [Contribute, ResultsWaitPage, Results]