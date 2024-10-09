from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'inequity_aversion'
    players_per_group = None
    num_rounds = 1
    
    menu1_choices = [
        {'A': {'你': 125, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 115, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 105, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 95, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 85, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 75, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 65, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 55, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 45, '他人': 150}, 'B': {'你': 100, '他人': 260}},
        {'A': {'你': 35, '他人': 150}, 'B': {'你': 100, '他人': 260}},
    ]
    
    menu2_choices = [
        {'A': {'你': 185, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 175, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 165, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 155, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 145, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 135, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 125, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 115, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 105, '他人': 90}, 'B': {'你': 170, '他人': 50}},
        {'A': {'你': 95, '他人': 90}, 'B': {'你': 170, '他人': 50}},
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 修改 make_field 方法，移除 label 参数
    def make_field():
        return models.StringField(
            choices=[['A', 'A'], ['B', 'B']],
            widget=widgets.RadioSelectHorizontal,
            label=""  # 使用空字符串作为标签
        )

    # 为 Menu1 创建 10 个字段
    menu1_choice_1 = make_field()
    menu1_choice_2 = make_field()
    menu1_choice_3 = make_field()
    menu1_choice_4 = make_field()
    menu1_choice_5 = make_field()
    menu1_choice_6 = make_field()
    menu1_choice_7 = make_field()
    menu1_choice_8 = make_field()
    menu1_choice_9 = make_field()
    menu1_choice_10 = make_field()

    # 为 Menu2 创建 10 个字段
    menu2_choice_1 = make_field()
    menu2_choice_2 = make_field()
    menu2_choice_3 = make_field()
    menu2_choice_4 = make_field()
    menu2_choice_5 = make_field()
    menu2_choice_6 = make_field()
    menu2_choice_7 = make_field()
    menu2_choice_8 = make_field()
    menu2_choice_9 = make_field()
    menu2_choice_10 = make_field()

    alpha = models.FloatField()
    beta = models.FloatField()
    alpha_interval = models.StringField()
    beta_interval = models.StringField()
    alpha_consistency = models.StringField()
    beta_consistency = models.StringField()
    
# PAGES
class Introduction(Page):
    pass


class Menu1(Page):
    form_model = 'player'
    
    @staticmethod
    def get_form_fields(player):
        return ['menu1_choice_' + str(i) for i in range(1, 11)]

    @staticmethod
    def vars_for_template(player):
        return {
            'choices': zip(Constants.menu1_choices, [f'menu1_choice_{i}' for i in range(1, 11)])
        }

class Menu2(Page):
    form_model = 'player'
    
    @staticmethod
    def get_form_fields(player):
        return ['menu2_choice_' + str(i) for i in range(1, 11)]

    @staticmethod
    def vars_for_template(player):
        return {
            'choices': zip(Constants.menu2_choices, [f'menu2_choice_{i}' for i in range(1, 11)])
        }

class CalculationWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            calculate_parameters(player)

def calculate_parameters(player: Player):
    def calculate_parameter(choices, thresholds):
        switch_points = []
        last_choice = choices[0]
        for i, choice in enumerate(choices[1:], 1):
            if choice != last_choice:
                switch_points.append(i)
                last_choice = choice
        
        if not switch_points:
            if choices[0] == 'A':
                return thresholds[-1], f">{thresholds[-1]}", "consistent"
            else:
                return thresholds[0], f"<{thresholds[0]}", "consistent"
        elif len(switch_points) == 1:
            i = switch_points[0]
            if i == 0:
                return thresholds[0], None, "consistent"
            elif i == len(choices) - 1:
                return (thresholds[-2] + thresholds[-1]) / 2, f"[{thresholds[-1]}, {thresholds[-2]}]", "consistent"
            else:
                return (thresholds[i-1] + thresholds[i]) / 2, f"[{thresholds[i]}, {thresholds[i-1]}]", "consistent"
        else:
            estimates = []
            for i in switch_points:
                if i == 0:
                    estimates.append(thresholds[0])
                else:
                    estimates.append((thresholds[i-1] + thresholds[i]) / 2)
            
            estimate = sum(estimates) / len(estimates)
            interval = f"[{min(thresholds[min(switch_points)-1:max(switch_points)+1])}, {max(thresholds[min(switch_points)-1:max(switch_points)+1])}]"
            return estimate, interval, "inconsistent"

    alpha_thresholds = [0.19, 0.12, 0.04, -0.05, -0.16, -0.29, -0.47, -0.69, -1.00, -1.44]
    beta_thresholds = [0.60, 0.14, -0.11, -0.27, -0.38, -0.47, -0.53, -0.58, -0.62, -0.65]

    alpha_choices = [getattr(player, f'menu1_choice_{i}') for i in range(1, 11)]
    beta_choices = [getattr(player, f'menu2_choice_{i}') for i in range(1, 11)]

    player.alpha, player.alpha_interval, player.alpha_consistency = calculate_parameter(alpha_choices, alpha_thresholds)
    player.beta, player.beta_interval, player.beta_consistency = calculate_parameter(beta_choices, beta_thresholds)

class Results(Page):
    pass  # 不再需要在这里进行计算

page_sequence = [Introduction, Menu1, Menu2, CalculationWaitPage, Results]