from selenium import webdriver
from time import sleep
import re



#browser : 瀏覽器


opt = webdriver.ChromeOptions() #建立選項物件

#加入 禁止顯示訊息框
opt.add_experimental_option( 'prefs' ,
      { 'profile.default_content_setting_values' : {'notifications' : 2}} )



browser = webdriver.Chrome( options = opt )

browser.get( "https://www.facebook.com/" )
"""
#操作
browser.find_element_by_id( 'email' ).send_keys( 'john08180818@yahoo.com.tw' )
browser.find_element_by_id( 'pass' ).send_keys( 'john0818' )
browser.find_element_by_id( 'loginbutton' ).click()
browser.find_element_by_class_name( '_1frb' ).send_keys("簡寬宇")
browser.find_element_by_class_name( '_585_' ).click()

sleep(3)
#browser.find_element_by_id('bluebarRoot')

'''
sleep(3)
browser.close() #關閉 selenium 開起的網頁
browser.quit() #關閉 selenium 開起的東西
'''
"""
