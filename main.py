import json
import translate
import time
import os
#json.dumps({"a":"§"})
#exit()


def TranslateArr(DataWaitToTransArr):
    
    ResultArr = []
    DataWaitToTrans = "\n\n".join(DataWaitToTransArr)
    Pos = 0
    EffectivePos = 0
    TranslatedPos = -2
    googletrans = translate.Translate()
    Finish = False
    #fw = open("test.txt","w")
    #fw.write(DataWaitToTrans)
        
    while True:
        while True:
            Pos = DataWaitToTrans.find("\n\n",Pos+1)
            if Pos == -1:
                EffectivePos = len(DataWaitToTrans)+1
                Finish = True
                break
            #print(Pos - TranslatedPos,Pos)
            if Pos - TranslatedPos > 5000:
                break
            EffectivePos = Pos
        
        #print("'"+DataWaitToTrans[TranslatedPos+2:EffectivePos]+"'")
        
        Transresult = googletrans.TransText(DataWaitToTrans[TranslatedPos+2:EffectivePos])
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
    

os.rename(r".minecraft\versions\Multiblock Madness\config\betterquesting\DefaultQuests.json",r".minecraft\versions\Multiblock Madness\config\betterquesting\DefaultQuests.bak.json")
fr = open(r".minecraft\versions\Multiblock Madness\config\betterquesting\DefaultQuests.bak.json","r")
RawData = fr.read()
fr.close()
JsonData = json.loads(RawData)
DataWaitToTransArr = []
for keys in JsonData["questDatabase:9"]:
    name = JsonData["questDatabase:9"][keys]["properties:10"]["betterquesting:10"]["name:8"]# name
    name = name.lstrip()
    if name == "":
        name = "No name"
    DataWaitToTransArr.append(name)
    
    text = JsonData["questDatabase:9"][keys]["properties:10"]["betterquesting:10"]["desc:8"]
    text = text.replace("搂","§")# text 替换 "搂"为§
    text = text.replace("危","Σ")
    text = text.replace("蟽","σ")
    text = text.replace("畏","η")
    text = text.replace("蟺","π")
    text = text.replace("\n","\\n")
    text = text.lstrip()
    Pos = -4
    while True:
        Pos = text.find("§",Pos+4)
        if Pos == -1:
            break
        text = text[:Pos+2]+" "+text[Pos+2:]
        #print(text)
    Pos = -2
    while True:
        Pos = text.find("\\",Pos+2)
        #print(Pos)
        if Pos == -1:
            break
        text = text[:Pos+2]+" "+text[Pos+2:]
        #print(text)
    text = text.lstrip()
    if text == "":
        text = "No Description"
    if len(text) >4980:
        text = "Too long, cannot be translated automaticly"
    DataWaitToTransArr.append(text)



TransResultArr = TranslateArr(DataWaitToTransArr)
i = 0
print("Final:",len(JsonData["questDatabase:9"]),len(TransResultArr))
for keys in JsonData["questDatabase:9"]:
    JsonData["questDatabase:9"][keys]["properties:10"]["betterquesting:10"]["name:8"] = TransResultArr[i]
    i += 1
    text = TransResultArr[i]
    i += 1
    text = text.replace("\\\\ n","\n")
    text = text.replace("\\\\n","\n")
    text = text.replace("\\ n","\n")
    text = text.replace("\\n","\n")
    JsonData["questDatabase:9"][keys]["properties:10"]["betterquesting:10"]["desc:8"] = text

RawData = json.dumps(JsonData,ensure_ascii = False)
#RawData = RawData.replace("\\u00a7","§")
#RawData = RawData.replace("\\u03a3","Σ")
#RawData = RawData.replace("\\u03c3","σ")
#RawData = RawData.replace("\\u03b7","η")
#RawData = RawData.replace("\\u03c0","π")
Pos = -2
while True:
    Pos = RawData.find("§",Pos+2)
    
    if Pos == -1:
            break
    RawData = RawData[:Pos+1]+RawData[Pos+1].lower()+RawData[Pos+2:]
fw = open(r".minecraft\versions\Multiblock Madness\config\betterquesting\DefaultQuests.json","wb")
fw.write(RawData.encode("UTF-8"))

fw.close()