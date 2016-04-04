# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import csv
from db import personal_status,english_gter
import time

with open('go_english_to_study_data.csv',"wb") as f:
    start_time=time.time()
    csv_writer=csv.writer(f)
    csv_writer.writerow([
                '申请学校',
                '学位',
                '专业',
                '申请结果',
                '入学年份',
                '入学学期',
                '通知时间',
                'IELTS',

                '本科学校档次',
                '本科专业',
                '本科成绩和算法，排名',
                '其他说明',
                'url'])
    for status in english_gter.objects:
        csv_writer.writerow([
            status.applied_school,
            status.degree,
            status.subject,
            status.applied_result,
            status.start_time,
            status.start_term,
            status.anonnced_time,
            status.ielts,

            status.undergraduate_school,
            status.undergraduate_subject,
            status.gpa,
            status.other_info,
            status.url
        ])
    print "to csv,it cost:",time.time()-start_time
