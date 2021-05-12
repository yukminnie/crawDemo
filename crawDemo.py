# coding=utf-8

from util import *
import urllib
import json
from lxml import etree
from pyquery import PyQuery as pq
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 遍历（方便遍历网址）
def lst(ul, nm):
    noun_list = [ul.format(i) for i in range(1,nm)]
    return noun_list


# 拼接 （方便拼接网址）
def add(li, lis):
    add_list = [li + str(l) for l in lis]
    return add_list

# testUrl
biliApiUrl = 'https://api.bilibili.com/x/space/arc/search?mid=1128859087&ps=30&tid=0&pn={}'

kbjApiUrl = 'https://bjapi.afreecatv.com/api/secretx/vods/all?page={}&per_page=60'

# 自动 headers
headers = get_headers()

# 手动 headers
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

# 请求
# r = requests.get(url, headers=headers,verify=False)


    
# r = requests.get(url, headers=headers)

# 请求为静态网页
# text = r.text

# 请求为动态网页 api
def parseJsonData(jsondata):
    jsontext = json.loads(jsondata)
    
    # kbjTest code
    # li = jsontext['data']
    # link_list = [l['title_no'] for l in li]
    # st = "https://vod.afreecatv.com/PLAYER/STATION/"
    
    # biliTest demo
    li = jsontext['data']['list']['vlist']
    link_list = [l['bvid'] for l in li]
    st = "https://www.bilibili.com/video/"
    
    parseList = add(st,link_list)   
    return parseList



def main():
    # req_list = lst(kbjApiUrl,8)
    req_list = lst(biliApiUrl,8)
    for l in req_list:
        r = requests.get(l, headers=headers)
        down_list = parseJsonData(r.text)
        print(down_list)
        print('\r\n')
        time.sleep(5)


if __name__ == '__main__':
    main()



