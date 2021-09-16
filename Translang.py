#coding:utf-8
import translate
fr = open("en_us.lang","r",encoding='utf-8')
RawData=fr.read()
fr.close()
DictHead = []
DictContext = []
for i in RawData.split("\n"):
    Data = i.split("=")
    DictHead.append(Data[0])
    DictContext.append(Data[1])
#print(len(DictHead))
#print(DictContext)
DictContext = translate.TranslateArr(DictContext)
#print(len(DictContext))
#print(DictContext)
FinalArray = []
for i in range(len(DictHead)):
    FinalArray.append(DictHead[i] + "=" + DictContext[i])
fw = open("zh_cn.lang","w",encoding='utf-8')
fw.write("\n".join(FinalArray))
fw.close()