from otree.api import *

doc = """
Choice list (Holt/Laury, risk preferences, price list, equivalence test, etc)
"""


class Constants(BaseConstants):
    name_in_url = 'longshot_loss'
    players_per_group = None
    num_rounds = 1
    table_template = __name__ + '/table.html'


def read_csv():
    import csv
    import random

    f = open(__name__ + '/stimuli.csv', encoding='utf-8-sig')
    rows = list(csv.DictReader(f))

#    random.shuffle(rows)
    return rows


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        stimuli = read_csv()
        for stim in stimuli:
            Trial.create(player=p, **stim)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    raw_responses = models.LongStringField()
    chose_lottery = models.BooleanField()
    won_lottery = models.BooleanField()


class Trial(ExtraModel):
    player = models.Link(Player)
    sure_payoff = models.CurrencyField()
    lottery_high = models.CurrencyField()
    lottery_low = models.CurrencyField()
    probability1 = models.FloatField()
    probability2 = models.FloatField()
    chose_lottery = models.BooleanField()
    randomly_chosen = models.BooleanField(initial=False)


# PAGES
class Introduction(Page):
    pass

class Stimuli(Page):
    form_model = 'player'
    form_fields = ['raw_responses']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(trials=Trial.filter(player=player))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import json
        import random

        trials = Trial.filter(player=player)

        # you could adjust this code to handle timeout_happened.
        responses = json.loads(player.raw_responses)
        for trial in trials:
            trial.chose_lottery = responses[str(trial.id)]

        trial = random.choice(trials)
        trial.randomly_chosen = True
        player.chose_lottery = trial.chose_lottery
        if player.chose_lottery:
            player.won_lottery = trial.probability1 > random.randrange(100)
            if player.won_lottery:
                payoff = -trial.lottery_high
            else:
                payoff = -trial.lottery_low
        else:
            payoff = -trial.sure_payoff
        player.payoff = -payoff


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        trials = Trial.filter(player=player, randomly_chosen=True)
        return dict(trials=trials)


page_sequence = [Introduction, Stimuli, Results]
