# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import gevent
import requests
from bs4 import BeautifulSoup
from engine import personal_status


def get_link(url):
    content=requests.get(url)
    soup=BeautifulSoup(content.text)
    url_list=soup.find_all('a')

    return_list=[]

    for item in url_list:
        if 'viewthread' in item['href']:
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
        td_list=status.find_all('td')
        i=0
        for item in status.find_all('th'):
            if item.get_text()=="TOEFL:":
                print td_list[i].get_text().strip()
            if item.get_text()=="GRE:":
                print td_list[i].get_text().strip()
            if item.get_text()=="本科学校档次:":
                print td_list[i].get_text().strip()
            if item.get_text()=="本科专业:":
                print td_list[i].get_text().strip()
            if item.get_text()=="本科成绩和算法、排名:":
                print td_list[i].get_text().strip()
            i=i+1


    summary_table=[]
    for item in table_list:
        if 'summary' in item.attrs:
            if 'offer' in item['summary']:
                summary_table.append(item)
    for summary in summary_table:
        td_list=summary.find_all("td")
        i=0
        for item in summary.find_all("th"):
            if item.get_text()=="申请学校:":
                print td_list[i].get_text().strip()
            if item.get_text()=="学位:":
                print td_list[i].get_text().strip()
            if item.get_text()=="专业:":
                print td_list[i].get_text().strip()
            if item.get_text()=="申请结果:":
                print td_list[i].get_text().strip()
            if item.get_text()=="入学年份:":
                print td_list[i].get_text().strip()
            if item.get_text()=="入学学期:":
                print td_list[i].get_text().strip()
            if item.get_text()=="通知时间:":
                print td_list[i].get_text().strip()
            i=i+1
