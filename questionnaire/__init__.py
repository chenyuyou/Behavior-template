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
    year_month = models.StringField()
    identification = models.StringField()
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

   
    fuage = models.IntegerField(label="13、您父亲的年龄？",min=0)
    muage = models.IntegerField(label="14、您母亲的年龄？",min=0)
    fumuhukoudi=models.StringField(label="15、您父母的户口登记地？请按照xx省xx市xx区（县）填写")
    hukouleixing = models.StringField(label="16、您父母的户口类型？",choices=["农业户口","非农户口"])
    fuedu = models.StringField(label="17、您父亲的教育水平？",choices=["未受过教育","小学","初中","高中","中专/技校","职业高中","大学专科","大学本科","研究生及以上"])
    muedu = models.StringField(label="18、您母亲的教育水平？",choices=["未受过教育","小学","初中","高中","中专/技校","职业高中","大学专科","大学本科","研究生及以上"])
    fuwork = models.StringField(label="19、您父亲的工作类型？",choices=["国家机关工作人员","企业中高级管理人员","教师、工程师、医生、律师","技术工人（包括司机）","生产制造业职工","商业与服务业职工","个体户","农民","渔民","无业、失业、下岗"])
    muwork = models.StringField(label="20、您母亲的工作类型？",choices=["国家机关工作人员","企业中高级管理人员","教师、工程师、医生、律师","技术工人（包括司机）","生产制造业职工","商业与服务业职工","个体户","农民","渔民","无业、失业、下岗"])
    
    
    xingquaihao = models.StringField(label="21、您最大的兴趣爱好？")
    shetuan = models.StringField(label="22、您参加的社团名称？")
    shetuantezheng = models.StringField(label="23、您参加的社团具有哪些特征？",choices=["团队合作和集体主义要求高与个人表现（主义）","个人表现（主义）胜过团队合作和集体主义","两者都强调"])
    dangyuan = models.StringField(label="24、您是党员么？",choices=["是","否"])
    ganbu = models.StringField(label="25、您是否为学生干部？",choices=["是","否"])
    xueshenghui = models.StringField(label="26、您是校（院）学生会成员么？",choices=["是","否"])
    ziranzaihai = models.StringField(label="27、您家乡面临的自然死亡风险是什么？",choices=["地震","水灾","台风","雪灾"])
    taifengpinlv = models.StringField(label="28、您上大学前经历的台风多么？",choices=["没有","较少，几年才一次","一年一次","一年两次","一年三次","一年四次及以上"])
    xinqing = models.StringField(label="29、您今天的心情怎么样？",choices=["非常开心","开心","不好不坏","不开心","非常不开心"])
    yumen = models.StringField(label="30、过去一周，你感到沮丧、郁闷，做什么事情都不能振奋的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    jinzhang = models.StringField(label="31、过去一周，你感到精神紧张的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    zuolibuan = models.StringField(label="32、过去一周，你感到坐卧不安、难以保持平静的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    meixiwang = models.StringField(label="33、过去一周，你感到未来没有希望的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    kunnan = models.StringField(label="34、过去一周，你做任何事情感到困难的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    shenghuoyiyi = models.StringField(label="35、过去一周，您认为生活没有意义的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
     



    changyongshou = models.StringField(label="36、您的常用手？",choices=["左手","右手"])
    jianzhi = models.StringField(label="37、您是否曾经兼职过？",choices=["是","否"])
    major = models.StringField(label="38、您的专业是？")
    xiaofei = models.IntegerField(label="38、您月消费？")
    xianxue = models.StringField(label="39、您是否主动献血过？",choices=["是","否"])
    xianxuetime = models.IntegerField(label="40、您的献血次数？",min=0)
    juankuan = models.StringField(label="41、您是否主动捐款过？",choices=["是","否"])
    experience = models.StringField(label="42、您是否参加过类似实验？",choices=["是","否"])
    shehuidiwei = models.IntegerField(label="43、如果社会最顶层用10表示，最底层用1表示，您认为自己属于什么社会位置？", min=1,max=10)
    banjidiwei = models.IntegerField(label="44、班级中，如果最顶层用10表示，最底层用1表示，您认为自己属于什么班级位置？", min=1,max=10)


class MyPage(Page):
    form_model = 'player'
#    form_fields = ['male', 'age','minzu','changyongshou','city','ganbu','jianzhi','major','fuqinedu','muqinedu','shouru','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']
    form_fields = ['male', 'age','minzu', 'identification', 'chushengdi', 'hukoudi', 'xiaoxuedi','chuzhongdi','gaozhongdi','gaokaochengji','shouru','xiongdi','fuage','muage','fumuhukoudi','hukouleixing',
                    'fuedu','muedu','fuwork','muwork','xingquaihao','shetuan','shetuantezheng','dangyuan','ganbu','xueshenghui','ziranzaihai','taifengpinlv','xinqing','yumen',
                    'jinzhang','zuolibuan','meixiwang','kunnan','shenghuoyiyi','changyongshou','jianzhi','major','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']

class QPage(Page):
    form_model = 'player'
    form_fields = ['brother_sister']
#   form_fields = ['male','year_month','identification','birth_province','birth_city','birth_district','hukou_province','hukou_city','hukou_district','three_province','three_city','three_district','primary_province',
#    'primary_city','primary_district','junior_province','junior_city','junior_district','high_province','high_city','high_district','language_score','math_score','english_score','other_score','provincial_ranking',
#    'household_income']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [QPage, ResultsWaitPage, Results]