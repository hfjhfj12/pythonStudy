#案例：演示JS三种弹出框的处理！

'''
三种：
confirm
prompt
alert
'''

from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

#让JS弹出框出现
ele1=driver.find_element_by_id("alerta")
ele1.click()

#开始处理JS弹出框
a=driver.switch_to.alert
print(a.text)
a.accept()

#输入账号
ele2=driver.find_element_by_id("userA")
ele2.send_keys("张三")

time.sleep(5)
driver.quit()