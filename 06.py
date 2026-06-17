#案例：演示Link_text定位法！

'''
说明：link_text定位与前面4个定位有所不同，它专门只用来定位超链接文本（<a>标签</a>）。

相关函数：
Ele find_element_by_link_text(String a标签的全部文本内容) //精确匹配a标签的文本内容
Eles find_elements_by_link_text(String a标签的全部文本内容) //精确匹配a标签的文本内容

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_a=driver.find_element(By.LINK_TEXT,"访问 新浪1 网站")
ele_a.click()

time.sleep(5)
driver.quit()