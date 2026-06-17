#案例：切换iframe框架，切换内嵌网页！


from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucesili.html")

#定位“注册实例”页面中的“账号”
user=driver.find_element_by_css_selector("#user")
user.send_keys("张三")


#切进去：注册A
ele_iframe=driver.find_element_by_id("idframe1")
driver.switch_to.frame(ele_iframe)

#操作“注册A”页面中的账号
userA=driver.find_element_by_css_selector("#userA")
userA.send_keys("张三A")

#切回来
driver.switch_to.default_content()

ele_pwd=driver.find_element_by_id("password")
ele_pwd.send_keys("123456")


time.sleep(5)
driver.quit()