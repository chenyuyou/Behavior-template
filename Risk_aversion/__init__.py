from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_rounds = 1
    
    choices = [
        {'A': {'p': 0.1, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.1, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.2, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.2, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.3, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.3, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.4, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.4, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.5, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.5, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.6, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.6, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.7, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.7, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.8, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.8, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 0.9, 'high': 2.00, 'low': 1.60}, 'B': {'p': 0.9, 'high': 3.85, 'low': 0.10}},
        {'A': {'p': 1.0, 'high': 2.00, 'low': 1.60}, 'B': {'p': 1.0, 'high': 3.85, 'low': 0.10}},
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    def make_field():
        return models.StringField(
            choices=[['A', 'A'], ['B', 'B']],
            widget=widgets.RadioSelectHorizontal,
            label=""
        )

    choice_1 = make_field()
    choice_2 = make_field()
    choice_3 = make_field()
    choice_4 = make_field()
    choice_5 = make_field()
    choice_6 = make_field()
    choice_7 = make_field()
    choice_8 = make_field()
    choice_9 = make_field()
    choice_10 = make_field()

    risk_aversion = models.FloatField()
    risk_aversion_interval = models.StringField()
    consistency = models.StringField()
    risk_pattern = models.StringField()


class Introduction(Page):
    pass

class RiskAversionTask(Page):
    form_model = 'player'
    form_fields = ['choice_' + str(i) for i in range(1, 11)]

    @staticmethod
    def vars_for_template(player):
        return {'choices': zip(Constants.choices, [f'choice_{i}' for i in range(1, 11)])}

class CalculationWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            calculate_risk_aversion(player)

def calculate_risk_aversion(player: Player):
    def calculate_parameter(choices):
        r_estimates = [-0.95, -0.49, -0.15, 0.15, 0.41, 0.68, 0.97, 1.37, 1.54]
        
        # 处理空白选择
        valid_choices = [c for c in choices if c in ['A', 'B']]
        if not valid_choices:
            return None, None, "invalid", "所有选择均为空白"

        switch_points = []
        last_choice = valid_choices[0]
        for i, choice in enumerate(valid_choices[1:], 1):
            if choice != last_choice:
                switch_points.append(i)
                last_choice = choice

        if not switch_points:
            if valid_choices[0] == 'A':
                return 1.54, ">1.54", "consistent", "极度风险厌恶"
            else:
                return -0.95, "<-0.95", "consistent", "极度风险寻求"
        elif len(switch_points) == 1:
            i = switch_points[0]
            if i == 0:
                return r_estimates[0], None, "consistent", "高度风险寻求"
            elif i == len(valid_choices) - 1:
                return (r_estimates[-2] + r_estimates[-1]) / 2, f"[{r_estimates[-2]}, {r_estimates[-1]}]", "consistent", "高度风险厌恶"
            else:
                r = (r_estimates[i-1] + r_estimates[i]) / 2
                interval = f"[{r_estimates[i-1]}, {r_estimates[i]}]"
                return r, interval, "consistent", "标准风险偏好"
        else:
            estimates = [r_estimates[i-1] for i in switch_points if i > 0]
            r = sum(estimates) / len(estimates)
            interval = f"[{min(estimates)}, {max(estimates)}]"
            return r, interval, "inconsistent", "不一致风险偏好"

    choices = [getattr(player, f'choice_{i}') for i in range(1, 11)]
    player.risk_aversion, player.risk_aversion_interval, player.consistency, player.risk_pattern = calculate_parameter(choices)

class Results(Page):
    pass

page_sequence = [Introduction, RiskAversionTask, CalculationWaitPage, Results]