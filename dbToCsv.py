# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import csv
from db import personal_status

with open('go_america_to_study_data.csv',"wb") as f:
    csv_writer=csv.writer(f)
    csv.writerow(['申请学校',
                '学位',
                '专业',
                '申请结果',
                '入学年份',
                '入学学期',
                '通知时间',
                'TOEFL',
                'GRE',
                '本科学校档次',
                '本科专业',
                '本科成绩和算法，排名',
                '其他说明',
                'url'])
    for status in personal_status.objects:
        csv.writerow([
            status.applied_school,
            status.degree,
            status.subject,
            status.applied_result,
            status.start_time,
            status.start_term,
            status.anonnced_time,
            status.toefl,
            status.gre,
            status.undergraduate_school,
            status.undergraduate_subject,
            status.gpa,
            status.other_info,
            status.url
        ])
