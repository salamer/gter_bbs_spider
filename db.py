import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


from mongoengine import *

class personal_status(Document):
    applied_school=StringField(max_length=100)
    degree=StringField(max_length=100)
    subject=StringField(max_length=100)
    applied_result=StringField(max_length=100)
    start_time=StringField(max_length=100)
    start_term=StringField(max_length=100)
    anonnced_time=StringField(max_length=100)


    toefl=StringField(max_length=100)
    gre=StringField(max_length=100)
    undergraduate_school=StringField(max_length=100)
    undergraduate_subject=StringField(max_length=100)
    gpa=StringField(max_length=100)


    url=StringField(max_length=100)
