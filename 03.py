#案例：演示name定位法！

'''
功能：是根据html元素的name属性的值来定位元素！

相关函数：
Ele driver.find_element_by_name(String name属性)
Eles driver.find_elements_by_name(String name属性)

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_zanhaoA=driver.find_element(By.NAME,"userA")
ele_zanhaoA.send_keys("张三A")

time.sleep(5)
driver.quit()