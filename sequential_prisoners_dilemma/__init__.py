from otree.api import *



doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'sequential_prisoners_dilemma'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'sequential_prisoners_dilemma/instructions.html'
    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = cu(140)
    betrayed_payoff = cu(60)
    # payoff if both players cooperate or both defect
    both_cooperate_payoff = cu(120)
    both_defect_payoff = cu(68)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decisionA = models.StringField(
    #    choices=[['Cooperate', '左'], ['Defect', '右']],
        choices=[['左', '左'], ['右', '右']],
        doc="""This player's decision""",
        widget=widgets.RadioSelectHorizontal, label="如果我是A，我选择："
    )

    decisionB1 = models.StringField(
    #    choices=[['Cooperate', '左'], ['Defect', '右']],
        choices=[['左', '左'], ['右', '右']],
        doc="""This player's decision""",
        widget=widgets.RadioSelectHorizontal, label="如果我是B，且A选择了左，那我选择："
    )
    decisionB2 = models.StringField(
    #    choices=[['Cooperate', '左'], ['Defect', '右']],
        choices=[['左', '左'], ['右', '右']],
        doc="""This player's decision""", 
        widget=widgets.RadioSelectHorizontal, label="如果我是B，且A选择了右，那我选择："
    )


# FUNCTIONS
def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)


def other_player(player: Player):
    return player.get_others_in_group()[0]


def set_payoff(player: Player):
    payoff_matrix = dict(
        左=dict(
#            Cooperate=Constants.both_cooperate_payoff, Defect=Constants.betrayed_payoff
            左=Constants.both_cooperate_payoff, 右=Constants.betrayed_payoff
        ),
        右=dict(
#            Cooperate=Constants.betray_payoff, Defect=Constants.both_defect_payoff
            左=Constants.betray_payoff, 右=Constants.both_defect_payoff
        ),
    )
    player.payoff = payoff_matrix[player.decisionA][other_player(player).decisionA]


# PAGES
class Introduction(Page):
    pass


class Decision(Page):
    form_model = 'player'
    form_fields = ['decisionA', 'decisionB1', 'decisionB2']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        me = player
        opponent = other_player(me)
        return dict(
            my_decisionA=me.decisionA,         
            opponent_decisionA=opponent.decisionA
        )


page_sequence = [Introduction, Decision, ResultsWaitPage, Results]
