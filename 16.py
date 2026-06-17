#案例：演示html弹出框！



from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://bbs.52studyit.net/")


#点击“登录”按钮，让弹出框出现
ele1=driver.find_element_by_css_selector("button.pn.vm")
ele1.click()
time.sleep(1)

#定位“弹出框上的账号输入框”
ele_zanhao=driver.find_element_by_css_selector("input[id^='username_']")
ele_zanhao.send_keys("老董")




time.sleep(5)
driver.quit()