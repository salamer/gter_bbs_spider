# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import gevent
import requests
from bs4 import BeautifulSoup
from db import personal_status,english_gter



def get_link(url):
    content=requests.get(url)
    soup=BeautifulSoup(content.text)
    url_list=soup.find_all('a')

    return_list=[]

    for item in url_list:
        if 'viewthread' in item['href'] and 'extra' in item['href']:
            if item['href'] not in return_list:
                return_list.append(item['href'])

    return return_list

def get_personal_data(url):

    res=requests.get(url)
    soup=BeautifulSoup(res.text)
    table_list=soup.find_all("table")

    personal_table=[]
    for item in table_list:
        if "summary" in item.attrs:
            if '个人情况' in item['summary']:
                personal_table.append(item)


    for status in personal_table:

        toefl=''
        gre=''
        undergraduate_school=''
        undergraduate_subject=''
        gpa=''
        other_info=''


        td_list=status.find_all('td')
        i=0
        for item in status.find_all('th'):
            if item.get_text()=="TOEFL:":
                toefl=td_list[i].get_text().strip()
            if item.get_text()=="GRE:":
                gre=td_list[i].get_text().strip()
            if item.get_text()=="本科学校档次:":
                undergraduate_school=td_list[i].get_text().strip()
            if item.get_text()=="本科专业:":
                undergraduate_subject=td_list[i].get_text().strip()
            if item.get_text()=="本科成绩和算法、排名:":
                gpa=td_list[i].get_text().strip()
            if item.get_text()=="其他说明:":
                other_info=td_list[i].get_text().strip()
            i=i+1


    summary_table=[]
    for item in table_list:
        if 'summary' in item.attrs:
            if 'offer' in item['summary']:
                summary_table.append(item)
    for summary in summary_table:


        applied_school=''
        degree=''
        subject=''
        applied_result=''
        start_time=''
        start_term=''
        anonnced_time=''


        td_list=summary.find_all("td")
        i=0
        for item in summary.find_all("th"):
            if item.get_text()=="申请学校:":
                applied_school=td_list[i].get_text().strip()
            if item.get_text()=="学位:":
                degree=td_list[i].get_text().strip()
            if item.get_text()=="专业:":
                subject=td_list[i].get_text().strip()
            if item.get_text()=="申请结果:":
                applied_result=td_list[i].get_text().strip()
            if item.get_text()=="入学年份:":
                start_time=td_list[i].get_text().strip()
            if item.get_text()=="入学学期:":
                start_term=td_list[i].get_text().strip()
            if item.get_text()=="通知时间:":
                anonnced_time=td_list[i].get_text().strip()
            i=i+1


        new_data=personal_status(
            toefl=toefl,
            gre=gre,
            undergraduate_school=undergraduate_school,
            undergraduate_subject=undergraduate_subject,
            gpa=gpa,
            other_info=other_info,

            applied_school=applied_school,
            degree=degree,
            subject=subject,
            applied_result=applied_result,
            start_time=start_time,
            start_term=start_term,
            anonnced_time=anonnced_time,
            url=url
        )

        new_data.save()

def get_data_from_english_bbs(url):

        res=requests.get(url)
        soup=BeautifulSoup(res.text)
        table_list=soup.find_all("table")

        personal_table=[]
        for item in table_list:
            if "summary" in item.attrs:
                if '个人情况' in item['summary']:
                    personal_table.append(item)


        for status in personal_table:

            ielts=''

            undergraduate_school=''
            undergraduate_subject=''
            gpa=''
            other_info=''


            td_list=status.find_all('td')
            i=0
            for item in status.find_all('th'):
                if item.get_text()=="IELTS:":
                    ielts=td_list[i].get_text().strip()
                if item.get_text()=="本科学校档次:":
                    undergraduate_school=td_list[i].get_text().strip()
                if item.get_text()=="本科专业:":
                    undergraduate_subject=td_list[i].get_text().strip()
                if item.get_text()=="本科成绩和算法、排名:":
                    gpa=td_list[i].get_text().strip()
                if item.get_text()=="其他说明:":
                    other_info=td_list[i].get_text().strip()
                i=i+1


        summary_table=[]
        for item in table_list:
            if 'summary' in item.attrs:
                if 'offer' in item['summary']:
                    summary_table.append(item)
        for summary in summary_table:


            applied_school=''
            degree=''
            subject=''
            applied_result=''
            start_time=''
            start_term=''
            anonnced_time=''


            td_list=summary.find_all("td")
            i=0
            for item in summary.find_all("th"):
                if item.get_text()=="申请学校:":
                    applied_school=td_list[i].get_text().strip()
                if item.get_text()=="学位:":
                    degree=td_list[i].get_text().strip()
                if item.get_text()=="专业:":
                    subject=td_list[i].get_text().strip()
                if item.get_text()=="申请结果:":
                    applied_result=td_list[i].get_text().strip()
                if item.get_text()=="入学年份:":
                    start_time=td_list[i].get_text().strip()
                if item.get_text()=="入学学期:":
                    start_term=td_list[i].get_text().strip()
                if item.get_text()=="通知时间:":
                    anonnced_time=td_list[i].get_text().strip()
                i=i+1


            new_data=english_gter(
                ielts=ielts,

                undergraduate_school=undergraduate_school,
                undergraduate_subject=undergraduate_subject,
                gpa=gpa,
                other_info=other_info,

                applied_school=applied_school,
                degree=degree,
                subject=subject,
                applied_result=applied_result,
                start_time=start_time,
                start_term=start_term,
                anonnced_time=anonnced_time,
                url=url
            )

            new_data.save()
