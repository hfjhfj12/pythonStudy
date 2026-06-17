#案例：演示className定位法！

'''
功能：是根据元素的class属性的来定位html元素！

Class属性的值可能有多个，用空格分隔！
<a class=”my1 my2”></a>

相关函数：
Ele find_element_by_class_name(String class属性的值)
Eles find_elements_by_class_name(String class属性的值)
注意：只要class属性包含有该值，就能定位到！

提醒：两个值不能一起放，否则定位不了！

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_phone=driver.find_element(By.CLASS_NAME,"telA")
ele_phone.send_keys("13760453683")

time.sleep(5)
driver.quit()