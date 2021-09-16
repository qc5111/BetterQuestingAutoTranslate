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
def TranslateArr(DataWaitToTransArr):
    
    ResultArr = []
    DataWaitToTrans = "\n\n".join(DataWaitToTransArr)
    Pos = 0
    EffectivePos = 0
    TranslatedPos = -2
    googletrans = Translate()
    Finish = False
    fw = open("test.txt","w",encoding='utf-8')
    fw.write(DataWaitToTrans)
        
    while True:
        while True:
            Pos = DataWaitToTrans.find("\n\n",Pos+1)
            if Pos == -1:
                EffectivePos = len(DataWaitToTrans)+1
                Finish = True
                break
            #print(Pos - TranslatedPos,Pos)
            if Pos - TranslatedPos > 4800:
                break
            EffectivePos = Pos
        
        #print("'"+DataWaitToTrans[TranslatedPos+2:EffectivePos]+"'")
        
        Transresult = googletrans.TransText(DataWaitToTrans[TranslatedPos+2:EffectivePos])
        #Transresult = ""
        #print(DataWaitToTrans[TranslatedPos+2:EffectivePos].split("\n\n"))
        print(len(DataWaitToTrans[TranslatedPos+2:EffectivePos].split("\n\n")),len(Transresult.split("\n\n")))
        if len(DataWaitToTrans[TranslatedPos+2:EffectivePos].split("\n\n")) != len(Transresult.split("\n\n")):
            print("Fail!!!!!!!!!!!!!")
        ResultArr.append(Transresult)
        TranslatedPos = EffectivePos
        if Finish:
            print(("\n\n".join(ResultArr)).split("\n\n"))
            return ("\n\n".join(ResultArr)).split("\n\n")
        time.sleep(8)


 
