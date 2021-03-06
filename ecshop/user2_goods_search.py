'''
case:登录状态，首页商品关键词搜索,购买
'''

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "http://192.168.1.120/upload/"

driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)                    #隐式等待10秒

# 点击登录，进入登录页面
driver.get(url=url)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"登录").click()

# 清空、输入信息，勾选保存，点击登录
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('wanghui')
driver.find_element(By.NAME,'password').send_keys('banxian123')
driver.find_element(By.ID,'remember').click()
driver.find_element(By.NAME,'submit').click()

# 搜索框输入关键词搜索
driver.back()
driver.find_element(By.ID,"keyword").clear()
driver.find_element(By.ID,"keyword").send_keys('毛衣')
driver.find_element(By.NAME,'imageField').click()

print('毛衣搜索成功')
driver.save_screenshot("D:\截图\登录状态购买\dl001.png")

driver.find_element(By.XPATH,'//form[@id="compareForm"]/div/div[2]/a/img').click()

# 查看详情,清空数量，输入数量，打印本店价格和促销价格
driver.find_element(By.XPATH,'//div[@id="imglist"]/a[1]/img').click()
driver.find_element(By.XPATH,'//div[@id="imglist"]/a[2]/img').click()
driver.find_element(By.XPATH,'//div[@id="imglist"]/a[3]/img').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[1]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[2]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[3]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[4]').click()

# 输入购买数量，点击购买
driver.find_element(By.ID,'number').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'number').send_keys('3')
selfprice = driver.find_element(By.ID,"ECS_SHOPPRICE").text
print("本店价格:",selfprice)
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()


# 点击结算中心
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()

# 选择配送方式、支付方式
driver.find_element(By.NAME,'shipping').click()
driver.find_element(By.NAME,'payment').click()
driver.find_element(By.CSS_SELECTOR,'div[id="ECS_ORDERTOTAL"]+div input:nth-child(1)').click()

# 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/a').click()

# 切换到我的订单页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])

# 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()

# 截图
driver.save_screenshot("D:\截图\登录状态购买\dl002.png")

driver.quit()