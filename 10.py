#案例：演示对web元素的基础操作：
# clear函数：清空某控件的输入值！
#send_keys函数：给某控件输入值！
#click函数：点击某控件！
from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

ele_zanhaoA=driver.find_element_by_id("userA")
ele_zanhaoA.send_keys("张三")
time.sleep(2)
ele_zanhaoA.clear()



time.sleep(5)
driver.quit()