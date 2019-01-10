from colorama import Fore,Back,Style
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import re

def main():

 def intro():
  print((Fore.CYAN+Style.BRIGHT+"\t\t\t\t\t------------------------------Openload Downloader------------------------------"))
  box_msg(''' Created by Gautham Prakash   @: gauthamp10@gmail.com''')
  print((Style.RESET_ALL))

 def print_lines():                                             #printing dotted lines
  print((Style.BRIGHT+Fore.GREEN+"-"*168))
  print((Style.RESET_ALL))

 def new_line():
  print("\n")

 def box_msg(msg):                                              #for printing text in a box
  print((Style.BRIGHT+Back.GREEN+Fore.WHITE))
  row = len(msg)
  h = ''.join(['+'] + ['-' *row] + ['+'])
  result= h + '\n'"|"+msg+"|"'\n' + h
  print(result)


 def box_msg2(msg):                                              #for printing text in a box2
  print((Style.BRIGHT+Fore.WHITE))
  row = len(msg)
  h = ''.join(['+'] + ['~' *row] + ['+'])
  result= h + '\n'"|"+msg+"|"'\n' + h
  print(result)


 def screen_clear():                                            #clearing terminal screen
  if os.name == 'nt':
   os.system('cls')
  else:
   os.system('clear')


 def find_id(url):                                             #to resove url using selenium
  print("Wait Please............")

  driver = webdriver.Chrome()
  driver.set_window_position(-3000, 0) 
  driver.get(open_url)
  data=driver.page_source
  soup=BeautifulSoup(data,'html.parser')
  stream=soup.find('p',attrs={'id':['DtsBlkVFQx']})
  driver.close()
  
  return stream.text

 screen_clear()
 intro()
 open_url=input(Style.BRIGHT+Fore.CYAN+"Enter Openload link: ")
 print((Style.RESET_ALL))												
 start = time.time()
 try:                                                                      #check whther input is a valid URl
  urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', open_url)
  if urls:
   id=find_id(open_url)
   url='https://openload.co/stream/'+id
   box_msg2('''Download Link: '''+url)
   new_line()
   print('It took', time.time()-start, 'seconds.')
   new_line()
  else:
   print("Entered string was not a url!!")
 except:
  print("Invalid URL.Please Retry with a valid openload url!..")



if __name__ == '__main__':                                       #Calling main(), the actual entry point for the scraper
    main()  
    exit(0) 







