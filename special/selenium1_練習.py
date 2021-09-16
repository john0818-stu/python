from selenium import webdriver
from time import sleep

#browser : 瀏覽器
browser = webdriver.Chrome()
browser.get( "https://www.google.com/" )

print( '標題 :' , browser.title )
print( '網址 :' , browser.current_url )
#print( browser.page_source[0:10]) #原始碼

print( "視窗 :" , browser.get_window_rect() )

sleep(0.5)
browser.set_window_rect( 200 , 100 , 500 , 250 )
print( "視窗 :" , browser.get_window_rect() )
sleep(0.5)
browser.maximize_window()
print( "視窗 :" , browser.get_window_rect() )
sleep(0.5)
browser.minimize_window()
print( "視窗 :" , browser.get_window_rect() )
sleep(0.5)

#sleep(5)
browser.close() #關閉 selenium 開起的網頁
browser.quit() #關閉 selenium 開起的東西
