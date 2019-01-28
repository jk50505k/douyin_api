#!/usr/bin/env python
# encoding: utf-8
import requests
import time
import random

header={'User-Agent': 'Aweme/25010 CFNetwork/902.2 Darwin/17.7.0'}

commentList=[]
cursor=0
more=1

def getAwemeIdByShortUrl(url):
    try:
        return requests.get(url, headers=header, allow_redirects=False).headers['location'].split("/video/")[1].split("/")[0]
    except:
        return ""

def getID(url):
    global aweme_id
    aweme_id = getAwemeIdByShortUrl(url)
    if aweme_id == "":
        print("短链接错误")
        #exit(-1)
        return "wrong url"
    return aweme_id



postParams={
    "aweme_id": '',
    "comment_style":  "2",
    "cursor": str(cursor),
    'count':'40',
    'aid':"1128"
}



def apiComment(aweme_id,cursor):
    comment={}
    postParams['cursor']=cursor
    postParams['aweme_id'] = str(aweme_id)
    r = requests.get("https://aweme.snssdk.com/aweme/v1/comment/list/", params=postParams, headers=header)
    resp = r.json()
    #print(resp)
    more = {'more':resp['has_more']}
    comments = resp['comments']
    for i in comments:
        comment[i['user']['nickname'] + '(' + i['user']['short_id'] + ')']=i['text']
    return comment,more


if __name__ == '__main__':
    pass
    #print(apiComment('6598428630131412232', 0))
    
