#案例：切换窗口！


from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucesili.html")

ele_zanhao=driver.find_element_by_id("user")
ele_zanhao.send_keys("张三")

#让“注册A”窗口出现
ele1=driver.find_element_by_id("ZCA")
ele1.click()
time.sleep(2)

#当前窗口切换到“注册A”窗口
driver.switch_to.window(driver.window_handles[-1])

#定位“注册A”窗口中的某控件
ele_zanhaoA=driver.find_element_by_id("userA")
ele_zanhaoA.send_keys("张三A")


time.sleep(5)
driver.quit()