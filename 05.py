#案例：演示tagName定位法！

'''
功能：是根据元素的标签名来定位！
某元素的标签名是它本身！p标签的标签名就是p！

相关函数：
Ele driver.find_element_by_tag_name(String 标签名);)
Eles driver.find_elements_by_tag_name(String 标签名);)

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_zanhaoA=driver.find_element(By.TAG_NAME,"input")
ele_zanhaoA.send_keys("张三A")

time.sleep(5)
driver.quit()