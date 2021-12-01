from otree.api import *

author = 'Your name here'

doc = """
调查问券
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    male = models.StringField()
    identification = models.StringField()
    nationality = models.StringField()
    nationality_other = models.StringField()
    birth_province=models.StringField()
    birth_city=models.StringField()
    birth_district=models.StringField()
    hukou_province=models.StringField()
    hukou_city=models.StringField()
    hukou_district=models.StringField()
    three_province=models.StringField()
    three_city=models.StringField()
    three_district=models.StringField()
    primary_province=models.StringField()
    primary_city=models.StringField()
    primary_district=models.StringField()
    junior_province=models.StringField()
    junior_city=models.StringField()
    junior_district=models.StringField()
    high_province=models.StringField()
    high_city=models.StringField()
    high_district=models.StringField()
    language_score=models.StringField()
    math_score=models.StringField()
    english_score=models.StringField()
    other_score=models.StringField()
    provincial_ranking=models.StringField()
    household_income = models.StringField()
    brother_sister = models.IntegerField()
    father_age = models.IntegerField()
    mother_age = models.IntegerField()


    family_province =models.StringField()
    family_city = models.StringField()
    family_district = models.StringField()
    hukou_type=models.StringField()
    father_edu=models.StringField()
    mother_edu=models.StringField()
    father_work=models.StringField()
    father_work_other=models.StringField()
    mother_work=models.StringField()
    mother_work_other=models.StringField()
    interests = models.StringField()
    societies_name = models.StringField()
    societies_feature = models.StringField()
    party_member = models.StringField()
    class_leader = models.StringField()
    student_union = models.StringField()
    death_risk = models.StringField()
    typhoon_risk = models.StringField()   
    
    
    

    feeling = models.StringField()
    frustrated = models.StringField()
    nervous = models.StringField()
    not_calm = models.StringField()
    hopeless = models.StringField()
    difficulty = models.StringField()
    no_meaning = models.StringField()
     



    dominant_hand = models.StringField()
    part_time = models.StringField()
    major = models.StringField()
    consumption = models.IntegerField()
    donate_blood = models.StringField()
    donate_blood_num = models.IntegerField()
    donate = models.StringField()
    experiment = models.StringField()
    social_status = models.IntegerField()
    class_status = models.IntegerField()


class MyPage(Page):
    form_model = 'player'
#    form_fields = ['male', 'age','minzu','changyongshou','city','ganbu','jianzhi','major','fuqinedu','muqinedu','shouru','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']
    form_fields = ['male', 'age','minzu', 'identification', 'chushengdi', 'hukoudi', 'xiaoxuedi','chuzhongdi','gaozhongdi','gaokaochengji','shouru','xiongdi','fuage','muage','fumuhukoudi','hukouleixing',
                    'fuedu','muedu','fuwork','muwork','xingquaihao','shetuan','shetuantezheng','dangyuan','ganbu','xueshenghui','ziranzaihai','taifengpinlv','xinqing','yumen',
                    'jinzhang','zuolibuan','meixiwang','kunnan','shenghuoyiyi','changyongshou','jianzhi','major','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']

class QPage(Page):
    form_model = 'player'
#    form_fields = ['male','identification','nationality','nationality_other']
    form_fields = ['male','identification','nationality','nationality_other','birth_province','birth_city','birth_district','hukou_province','hukou_city','hukou_district','three_province','three_city','three_district','primary_province',
    'primary_city','primary_district','junior_province','junior_city','junior_district','high_province','high_city','high_district','language_score','math_score','english_score','other_score','provincial_ranking',
    'household_income','brother_sister','father_age','mother_age','family_province','family_city','family_district','hukou_type','father_edu','mother_edu','father_work','father_work_other','mother_work','mother_work_other',
    'interests','societies_name','societies_feature','party_member','class_leader','student_union','death_risk','typhoon_risk','feeling','frustrated','nervous','not_calm','hopeless','difficulty','no_meaning',
     'dominant_hand','part_time','major','consumption','donate_blood','donate_blood_num','donate','experiment','social_status','class_status']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [QPage, ResultsWaitPage, Results]