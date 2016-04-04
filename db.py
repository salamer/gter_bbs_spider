import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from config import db_name


from mongoengine import *
connect(db_name)

class personal_status(Document):
    applied_school=StringField()
    degree=StringField()
    subject=StringField()
    applied_result=StringField()
    start_time=StringField()
    start_term=StringField()
    anonnced_time=StringField()


    toefl=StringField()
    gre=StringField()
    undergraduate_school=StringField()
    undergraduate_subject=StringField()
    gpa=StringField()
    other_info=StringField()


    url=StringField()

class english_gter(Document):
    applied_school=StringField()
    degree=StringField()
    subject=StringField()
    applied_result=StringField()
    start_time=StringField()
    start_term=StringField()
    anonnced_time=StringField()


    ielts=StringField()

    undergraduate_school=StringField()
    undergraduate_subject=StringField()
    gpa=StringField()
    other_info=StringField()


    url=StringField()
