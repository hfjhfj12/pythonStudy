#案例:演示Xpath定位法！

'''
功能：根据Xpath语法来定位html标签！

相关函数：
Ele driver.find_element_by_xpath(String xpath)
Eles driver.find_elements_by_xpath(String xpath)
'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

#演示：绝对xpath
# ele=driver.find_element(By.XPATH,"/html/body/form/div/fieldset/p[1]/input")
# ele.send_keys("哈哈")

# #演示：精确关系：//*[@属性名='属性全部值']
# //表示从任意位置选取后代节点，*表示匹配任意节点，@表示选取属性
# ele=driver.find_element(By.XPATH,"//*[@name='userA']")
# ele.send_keys("哈哈")

#演示：精确关系：//标签名[@属性名='属性全部值']
# ele=driver.find_element_by_xpath("//input[@id='userA']")
# ele.send_keys("哈哈")


#演示：精确+层级：类似//*[@id='p1']/input
# ele=driver.find_element(By.XPATH,"//p[@id='p1']/input")
# ele.send_keys("哈哈")

#演示：精确+层级+属性：类似：//p[@id='p1']/input[@id='userA']
# ele=driver.find_element_by_xpath("//p[@id='p1']/input[@id='userA']")
# ele.send_keys("哈哈")

#演示：精确+多属性：类似//input[@class='login-test' and @name='user']
# ele=driver.find_element_by_xpath("//input[@name='userA' and @id='userA']")
# ele.send_keys("哈哈")

#注意：class属性的值必须给全部值，比如:@class=’my1 my2’
#<input type="telA" name="telA" id="telA" placeholder="电话A" class="telA telB" value="">
# ele_phone=driver.find_element_by_xpath("//input[@class='telA telB']")
# ele_phone.send_keys("13760453683")

#演示：多属性并且：类似//input[@name='userA' and contains(@placeholder,'号A')]
# ele=driver.find_element(By.XPATH,"//input[@name='userA' and contains(@placeholder,'号A')]")
# ele.send_keys("哈哈")


#演示：包含关系
# ele=driver.find_element_by_xpath("//input[contains(@placeholder,'邮箱')]")
# ele.send_keys("851286894@qq.com")

#演示：属性以xxx开头：//*[starts-with(@属性名,'开头的值')]
# ele=driver.find_element_by_xpath("//input[starts-with(@placeholder,'电子')]")
# ele.send_keys("851286894@qq.com")

# 演示：文本内容精确匹配！//*[text()=’全部文本内容’]
# ele=driver.find_element(By.XPATH,"//a[text()='访问 新浪1 网站']")
ele=driver.find_element(By.XPATH,"//a[text()='AA 新浪2 网站']")
# ele=driver.find_element(By.XPATH,"//p/a[@href='http://www.sina2.com.net']")
ele.click()

# ele=driver.find_element_by_xpath("//button[@value='注册A'][@title='加入会员A']") #OK
# ele=driver.find_element_by_xpath("//button[@value='注册A' and @title='加入会员A']")
# ele.click()


time.sleep(5)
driver.quit()