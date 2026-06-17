#案例：演示ID定位法！

'''
功能：根据元素的id属性来定位一个元素！

注意：元素的id属性是唯一的！

相关函数：
Ele driver.find_element_by_id(String id值)

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_zanhaoA=driver.find_element(By.ID,"userA")
ele_zanhaoA.send_keys("张三A")


time.sleep(5)
driver.quit()