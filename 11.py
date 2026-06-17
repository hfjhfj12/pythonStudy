#案例：

# 2.ele.text属性                 //获取html元素的文本内容（title标签不行）
# 3. driver.title属性                // 获取页面的窗口标题（前提：driver应该是当前窗口，注意切换窗口）
# 4.driver. current_url属性            //获取当前页面网址
# 5. String ele.get_attribute("xxx")方法   //获取html元素的某属性的值;xxx：要获取的属性
# 例子：
# <input value=”” class=”my1 my2”/>
# a=ele.get_attribute(“value”) #a=””,而不是a=None
# b=ele.get_attrbute(“class”) #b=”my1 my2”
#
#
# 6. ele.is_displayed()方法            判断html元素是否可见
# 7. ele.is_enabled()方法            判断html元素是否可用
# 8.ele.is_selected()方法，用于单选按钮、复选框，是否是选中状态

'''
功能：根据元素的id属性来定位一个元素！

注意：元素的id属性是唯一的！

相关函数：
Ele driver.find_element_by_id(String id值)

'''

from selenium import webdriver  # 导入webdriver包
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/zucea.html")

#演示：text属性
# ele=driver.find_element(By.CSS_SELECTOR,"#zc > fieldset > button")
# print(ele.text)

#演示：获取当前窗口标题
# print(driver.title)

#演示：获取当前窗口的url
# print(driver.current_url)
#
# #演示：获取某元素的某属性
# ele=driver.find_element(By.CSS_SELECTOR,"#zc > fieldset > button")
# attr_value=ele.get_attribute("value")
# print(attr_value)

#演示：演示判断元素是否是可见的
# ele=driver.find_element_by_tag_name("span")
# print(ele.is_displayed())

#


time.sleep(5)
driver.quit()