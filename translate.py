from selenium import webdriver
from urllib import parse
import time
class Translate():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def TransText(self,text):
        text = parse.quote(text)
        #print("https://translate.google.cn/?sl=en&tl=zh-CN&op=translate&text=%s" % text)
        self.driver.get("https://translate.google.cn/?sl=en&tl=zh-CN&op=translate&text=%s" % text)
        while True:
            try:
                ResultElement = self.driver.find_element_by_css_selector("div.J0lOec")
                break
            except:
                time.sleep(0.2)
        Result = ResultElement.get_attribute("innerText")
        self.driver.get("data:,")
        return Result
            
        
#Tras = Translate()
#result = Tras.TransText("This is a test.")
#print(result)



 
