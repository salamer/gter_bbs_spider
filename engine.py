import gevent.monkey
gevent.monkey.patch_socket()

import gevent

import crawler

import time

from config import start_url,page_number


def asyn_fetch(url_list):
    greenlets=[]
    for url in url_list:
        greenlets.append(gevent.spawn(crawler.get_data_from_english_bbs,url))
    gevent.joinall(greenlets)

if __name__=="__main__":
    start_time=time.time()
    for number in page_number:
        the_url=start_url+str(number)
        url_list=crawler.get_link(the_url)
        asyn_fetch(url_list)
        print the_url

    end_time=time.time()

    print "it cost:",start_time-end_time
