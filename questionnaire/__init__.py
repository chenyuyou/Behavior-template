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
    male = models.StringField(label="1、您的性别？",choices=["男","女"])
    age = models.IntegerField(label="2、您的年纪？",min=14,max=99)
    minzu = models.StringField(label="3、您的民族？")
    chushengdi=models.StringField(label="4、您的出生地？请按照xx省xx市xx区（县）填写")
    hukoudi=models.StringField(label="5、您的户口登记地？请按照xx省xx市xx区（县）填写")
    sansuidi=models.StringField(label="6、您三岁时居住地在哪？请按照xx省xx市xx区（县）填写")
    xiaoxuedi=models.StringField(label="7、您小学在哪里上的？请按照xx省xx市xx区（县）填写")
    chuzhongdi=models.StringField(label="8、您初中在哪里上的？请按照xx省xx市xx区（县）填写")
    gaozhongdi=models.StringField(label="9、您高中在哪里上的？请按照xx省xx市xx区（县）填写")
    gaokaochengji = models.StringField(label="10、您的高考各科成绩以及全省排名")

    shouru = models.IntegerField(label="11、您的家庭年收入？")
    xiongdi = models.IntegerField(label="12、您有几个兄弟姐妹？",min=0)
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
    taifengpinlv = models.StringField(label="28、您上大学前经历的台风多么？",choices=["没有","一年一次","一年两次","一年三次","一年四次及以上"])
    xinqing = models.StringField(label="29、您今天的心情怎么样？",choices=["非常开心","开心","不好不坏","不开心","非常不开心"])
    yumen = models.StringField(label="30、过去一周，你感到沮丧、郁闷，做什么事情都不能振奋的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    jinzhang = models.StringField(label="31、过去一周，你感到精神紧张的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    zuolibuan = models.StringField(label="32、过去一周，你感到坐卧不安、难以保持平静的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    meixiwang = models.StringField(label="33、过去一周，你感到未来没有希望的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    kunnan = models.StringField(label="34、过去一周，你做任何事情感到困难的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
    shenghuoyiyi = models.StringField(label="35、过去一周，您认为生活没有意义的频率？",choices=["几乎每天","有四五天","两三天","有一天","从来没有过"])
     



    changyongshou = models.StringField(label="3、您的常用手？",choices=["左手","右手"])
    jianzhi = models.StringField(label="6、您是否曾经兼职过？",choices=["是","否"])
    major = models.StringField(label="7、您的专业是？")
    xiaofei = models.IntegerField(label="11、您月消费？")
    xianxue = models.StringField(label="12、您是否主动献血过？",choices=["是","否"])
    xianxuetime = models.IntegerField(label="13、您的献血次数？",min=0)
    juankuan = models.StringField(label="14、您是否主动捐款过？",choices=["是","否"])
    experience = models.StringField(label="15、您是否参加过类似实验？",choices=["是","否"])
    shehuidiwei = models.IntegerField(label="16、如果社会最顶层用10表示，最底层用1表示，您认为自己属于什么社会位置？", min=1,max=10)
    banjidiwei = models.IntegerField(label="17、班级中，如果最顶层用10表示，最底层用1表示，您认为自己属于什么班级位置？", min=1,max=10)


class MyPage(Page):
    form_model = 'player'
#    form_fields = ['male', 'age','minzu','changyongshou','city','ganbu','jianzhi','major','fuqinedu','muqinedu','shouru','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']
    form_fields = ['male', 'age','minzu', 'chushengdi', 'hukoudi', 'xiaoxuedi','chuzhongdi','gaozhongdi','shouru','xiongdi','fuage','muage','fumuhukoudi','hukouleixing',
                    'fuedu','muedu','fuwork','muwork','xingquaihao','shetuan','shetuantezheng','dangyuan','ganbu','xueshenghui','ziranzaihai','taifengpinlv','xinqing','yumen',
                    'jinzhang','zuolibuan','meixiwang','kunnan','shenghuoyiyi','changyongshou','jianzhi','major','xiaofei','xianxue','xianxuetime','juankuan','experience','shehuidiwei','banjidiwei']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]