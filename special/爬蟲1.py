
import requests as rq
from bs4 import BeautifulSoup
import numpy as np

url = ""
data = rq.get( "https://www.facebook.com/pg/%E9%9D%A0%E5%8C%97%E4%B8%AD%E5%A4%AE-1514597625469099/posts/" )
soup = BeautifulSoup( data.text , "lxml" )
test = soup.select( "body div._li div#globalContainer div#content div div.clearfix div div#content_container div.clearfix div div#pagelet_timeline_main_column div div div._1xnd div p" )

for x in test :
    
    print( x.text )
'''
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

  
tStart = time.time()#計時開始
#fp = io.open("marryData-List.txt", "ab+")
for i in range( 1 , 2 ) : 
    nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg"+str(i)+"mm"
    nl_response = rq.get(nextlink) # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(nl_response.text, "lxml") # 指定 lxml 作為解析器
    for url in soup.findAll('a', {'class': 'shop_name'}):

        response = rq.get(url.get('href')+"#studio_about") # 用 requests 的 get 方法把網頁抓下來
        html_doc = response.text # text 屬性就是 html 檔案
        soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
        print( soup.select("h1")[0].find('a').text )

        pid = soup.findAll( 'li' , { "class" : "icon-check" } )
        Con = ",".join([p.text.strip()  for p in pid])
        
        print( Con )
        
    print(i)
tEnd = time.time()#計時結束
#fp.close()
print ("It cost %f sec" % (tEnd - tStart))#會自動做近位
'''
