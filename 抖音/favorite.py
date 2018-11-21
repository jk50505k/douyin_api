import requests

import time
import random
header={'User-Agent': 'Aweme/25010 CFNetwork/902.2 Darwin/17.7.0'}

max_cursor=0



postParams={
    "user_id": '',
    'count' : '21' ,
    'max_cursor' : str(max_cursor),
    'min_cursor':'0',
    'aid':'1128'
    
}



def getUrl(urlList):
    global playList
    playList=[]
    for i in urlList:
        address=i['video']['play_addr']['url_list'][0]
        playList.append(address)
        #print(address)

def getFavorite(user_id,max_cursor):
    postParams['user_id']=str(user_id)
    r = requests.get("https://aweme.snssdk.com/aweme/v1/aweme/favorite/?", params=postParams,  headers=header)
    result = r.json()
    #print(result)
    getUrl(result['aweme_list'])
    more = result['has_more']
    if more == 1:
        max_cursor = result['max_cursor']
        getFavorite(user_id,max_cursor)

def apiFavorite(user_id,max_cursor):
    postParams['user_id']=str(user_id)
    r = requests.get("https://aweme.snssdk.com/aweme/v1/aweme/favorite/?", params=postParams,headers=header)
    result = r.json()
    
    getUrl(result['aweme_list'])
    max_cursor = {'max_cursor':result['max_cursor']}
    more = {'more': result['has_more']}
    return playList,max_cursor,more

if __name__ == '__main__':
    pass
    #getFavorite(59189910855,max_cursor)

    #print(apiFavorite(59189910855,1541856489000))
