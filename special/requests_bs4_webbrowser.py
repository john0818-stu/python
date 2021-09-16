import requests
import bs4
import webbrowser #webbrowser.open( new.url ) 呼叫網頁

my_params = {'q': input("> ")}

r = requests.get( "https://www.google.com.tw/search" , params = my_params )
soup = bs4.BeautifulSoup( r.text , 'html.parser' )


#"""
title_tag = soup.title
print( title_tag )
print( title_tag.string )

a_tag = [ x.string for x in soup.find_all( 'a' , limit = 5 ) ]
print( a_tag )
#"""

"""
tag = soup.select( 'div#main div.ZINbbc.xpd.O9g5cc.uUPGi div.kCrYT div.BNeawe.vvjwJb.AP7Wnd')
href= soup.select( 'div#main div.ZINbbc.xpd.O9g5cc.uUPGi div.kCrYT a' )

n_href = [ x['href'].split("/url?q=")[1].split("&")[0] for x in href if 'BNeawe vvjwJb AP7Wnd' in str(x) ]

n_tag = [ x.string for x in tag ]

n = zip( n_href , n_tag )

for x in n :

  print( x[0] )
  print( x[1] )
  print()
  
#"""







#webbrowser.open( r.url )
