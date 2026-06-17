#案例：演示Partial_link_text定位法！

'''
说明：partial_link_text定位是对link_text定位的补充，partial_like_text为模糊匹配；link_text全部匹配！
也是只用于定位超链接标签a！

相关函数：
Ele find_element_by_partial_link_text(String a标签的部分文本内容)
Eles find_elements_by_partial_link_text(String a标签的部分文本内容)
说明：形参最好能表达唯一性的局部文本内容！
'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_a=driver.find_element(By.PARTIAL_LINK_TEXT,"新浪1")
ele_a.click()


time.sleep(5)
driver.quit()