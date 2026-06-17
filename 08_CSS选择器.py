#案例:演示CSS选择器定位法！

'''
功能：根据CSS选择器语法来定位html标签！

相关函数：
Ele driver.find_element_by_css_selector(String css选择器)
Eles driver.find_elements_by_css_selector(String css选择器)
'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

# 演示：id定位:格式:#id
# ele=driver.find_element(By.CSS_SELECTOR,"#userA")
# ele.send_keys("哈哈")

#演示：class定位:格式: .class
# ele=driver.find_element(By.CSS_SELECTOR,".telA.telB")
# ele.send_keys("13760453683")

#演示：标签名定位
# ele=driver.find_elements(By.CSS_SELECTOR,"input")[4]
# ele.send_keys("123456")

#演示：属性定位：类似[href]
# ele=driver.find_element(By.CSS_SELECTOR,"[href]")
# ele.click()

#演示：属性定位：类似[href='xxx']
# ele=driver.find_element(By.CSS_SELECTOR,"[href='http://www.sina1.com.cn']")
# ele.click()

#演示：属性定位：类似[href^='xxx']  [name^="user"]	name 属性以 "user" 开头
# driver.find_elements(By.CSS_SELECTOR,"[href^='http://']")[1].click()

#演示：属性定位：类似[href$='xxx']  [name$="mail"]	name 属性以 "mail" 结尾
# ele=driver.find_element(By.CSS_SELECTOR,"[href$='.com']")
# ele.click()

#演示：属性定位：类似[href*='xxx']
# ele=driver.find_element(By.CSS_SELECTOR,"[href*='taobao']")
# ele.click()


#演示：分组定位
# eles=driver.find_elements(By.CSS_SELECTOR,"input,a") # 在页面中查找所有 input 标签和所有 a 标签，并以列表形式返回这些 WebElement 对象。
# ele=eles[5]
# ele.click()

#演示：子标签定位 a>b(下一代)
# ele=driver.find_element(By.CSS_SELECTOR,"p#p1 > input[name='userB']")
# ele=driver.find_element(By.CSS_SELECTOR,"button[type='submitA']").click()
# ele.send_keys("哈哈")

#演示：后代标签定位 a b  （下几代）
# driver.find_element(By.CSS_SELECTOR,"div#zc input[name='userB']").send_keys("123456")

#演示：同辈相邻兄弟: a + b
# ele=driver.find_element(By.CSS_SELECTOR,"p#p1 + p > input")
# ele.send_keys("123456")

#演示：同辈兄弟：a ~ b
# eles=driver.find_elements(By.CSS_SELECTOR,"p#p1 ~ p")
# ele_p=eles[1]
# ele_input=ele_p.find_element(By.CSS_SELECTOR,"input")
# ele_input.send_keys("13760453683")

#演示：同辈兄弟：a ~ b：先计数，再判断第N个是否是p标签  不看
# ele_tel=driver.find_element_by_css_selector("p#p1 ~  p:nth-child(4) > input")
# ele_tel.send_keys("13760453683")

# 演示：:nth-child(N)   第几个孩子
ele=driver.find_element(By.CSS_SELECTOR,"fieldset > p:nth-child(3) > input")
ele.send_keys("12344")



time.sleep(5)
driver.quit()