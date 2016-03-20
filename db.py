from mongoengine import *

class personal_status(Document):
    applied_school=StringField(max_length=100)
    degree=StringField(max_length=100)
    subject=StringField(max_length=100)
    applied_result=StringField(max_length=50)
    start_time=StringField(max_length=50)
    start_term=StringField(max_length=50)
    anonnced_time=StringField(max_length=50)


    toefl=StringField(max_length=50)
    gre=StringField(max_length=50)
    undergraduate_school=StringField(max_length=50)
    undergraduate_subject=StringField(max_length=50)

    gpa=StringField(max_length=50)
