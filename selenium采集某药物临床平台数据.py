# 6.采集某药物临床平台数据信息
# 地址:http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml需求:使用selenium，采集所有数据采集字段:登记号+试验状态+药物名称+适应症+试验通俗题目+点击对应药物名称(申请联系人+首次公示信息日期+申请人名称)数据存储方案:csV、excel二者选一
from selenium import webdriver
import json


mobileEmulation = {'deviceName': 'iPhone 6/7/8'}   #设置手机环境
options = webdriver.ChromeOptions()
options.add_argument('headless')    #设置不显示页面
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('mobileEmulation', mobileEmulation)
#executable_path 为chromedriver文件路径，chromedriver是谷歌浏览器驱动软件
driver = webdriver.Edge()
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

i=109228
print("爬取第%d个" % i)
url = 'http://mobile.nmpa.gov.cn/datasearch/QueryRecord?tableId=25&searchF=ID&searchK=' + str(i)
driver.get(url)
xpath_drug = "//body"
data = driver.find_elements_by_xpath(xpath_drug)

#清洗获取的数据，tag = True 是数据不为空
info = ""
tag = True
for i2 in data:
    if i2.text == "[]":
        tag = False
    else:
        info += str(i2.text)
if tag == True:
    d = info.split("},{")
    info = "},{".join(d[:-1]) + "}]"
    Data = json.loads(info)
    print(Data)
#关闭
driver.quit()