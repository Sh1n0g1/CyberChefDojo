#Run CyberChef from Python using Selenium + Headless Chrome

# requirement:
# selenium (pip install selenium)
# google-chrome (apt install google-chrome)
# chrome web driver (http://chromedriver.chromium.org/downloads)
#   -> wget and unzip it.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
WEBDRIVERPATH='/usr/local/bin/chromedriver'
CYBERCHEF_URL='https://gchq.github.io/CyberChef/'

def cyberchef(input, recipe=''):
  input=input.encode('base64').replace('=','')
  options=Options()
  options.add_argument('--headless')
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(
    executable_path = WEBDRIVERPATH,
    chrome_options  = options
  )

  url=CYBERCHEF_URL+'#input='+input
  if recipe!='':
    url+='&recipe='+recipe
  driver.get(url)
  output=driver.find_element_by_id('output-text')
  time.sleep(0.5)
  result=output.get_attribute('value')

  return result

#sample

recipe='''XOR({'option':'Hex','string':'01'},'Standard',false)'''
input='udru032'
print cyberchef(input, recipe) # 'test123'



