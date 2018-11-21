import requests

import time
import random
from bs4 import BeautifulSoup
import re

header = {'User-Agent': 'Aweme/25010 CFNetwork/902.2 Darwin/17.7.0'}

max_time='1538215804'#第一页


postParams = {
    "user_id": str(''),
    'count': '20',
    'max_time': str(max_time),
    'aid':'1128'
}



followersList=[]
def getFollower(user_id,max_time):
    postParams['user_id']=user_id
    r = requests.get("https://aweme.snssdk.com/aweme/v1/user/follower/list/", params=postParams ,headers=header)
   # print(r.url)
    result = r.json()
    print(result)
    # if result['status_code']==2151:
    #     getFollower(user_id,max_time)
    #     time.sleep(0.5)
    more=result['has_more']
    followers = result['followers']
    for i in followers:
        followersList.append(i['nickname' ] + ':' + i['short_id'])
    if more ==True:
        max_time = result['min_time']
        getFollower(user_id,max_time)
        time.sleep(random.random()*2)
    if more== False:
        print(result)

def apiFollower(user_id,max_time):
    follower={}
    postParams['user_id'] = user_id
    r = requests.get("https://aweme.snssdk.com/aweme/v1/user/follower/list/", params=postParams, headers=header)
    #print(r.url)
    result = r.json()
    more = {'more':result['has_more']}
    followers = result['followers']
    max_time = {'max_time':result['min_time']}
    for i in followers:
        follower[i['nickname']]=i['short_id']
    return follower,more,max_time

def getParam(link):
    r=requests.get(link,headers=header)
    soup=BeautifulSoup(r.content,'html.parser')
    script=soup.find_all('script',attrs={'type':'text/javascript'})
    uid_t = re.findall(r'uid\: \"[0-9]+\"', str(script[2]))
    uid=re.findall(r'\d+',uid_t[0])[0]
    #print(uid)
    return uid

# getFollower('15',max_time)
# print(len(followersList))
# print(followersList)
#print(apiFollower(getParam('http://v.douyin.com/dv8GHj/'), max_time))
