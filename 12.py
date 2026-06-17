#案例：演示鼠标的常见操作！


from selenium import webdriver  # 导入webdriver包
import time
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

#演示鼠标单击
# ele_reg=driver.find_element_by_css_selector("#zc > fieldset > button")
# ActionChains(driver).click(ele_reg).perform()

#演示：鼠标双击
# ele_userA=driver.find_element_by_css_selector("#userA")
# ele_userA.send_keys("张三")
# time.sleep(2)
# ActionChains(driver).double_click(ele_userA).perform()

#演示：鼠标悬停在某元素上
# ele_reg=driver.find_element_by_css_selector("#zc > fieldset > button")
# ActionChains(driver).move_to_element(ele_reg).perform()


time.sleep(5)
driver.quit()