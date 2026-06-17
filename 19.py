#案例：常用控件的常用自动化操作！非封装版！

from selenium import webdriver  # 导入webdriver包
import time,os
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()


driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(10)

driver.get("http://oss.52studyit.net/webzdh/form.html")  # 通过get()方法，打开一个url站点

#控件：文本框：输入数据或清空
# ele=driver.find_element_by_id("username")
# ele.send_keys("张三")
# ele.click()


#控件：密码框：输入数据或清空
# ele=driver.find_element_by_id("pwd")
# ele.send_keys("123456")
# ele.clear()

#控件：选中某选项、或 获取当前选中的选项是谁
# <input type="radio" name="sex" value="F" />女
#说明：一般是根据name属性和你想要选中的某选项的value的值来定位
#选中
# name="sex" #这一组单选按钮的name属性的值
# option_value="F" #你想要选中的单选按钮的value属性的值
# ele_option=driver.find_element_by_css_selector(f"input[type='radio'][name='{name}'][value='{option_value}']")
# ele_option.click()

#获取当前选中是谁
# name="sex" #这一组单选按钮的name属性的值
# eles_option=driver.find_elements_by_css_selector(f"input[type='radio'][name='{name}'][value]")
# for ele in eles_option:
#     isXuanzon=ele.is_selected()
#     if isXuanzon:
#         attr_value=ele.get_attribute("value")
#         print("当前选中的选项的value属性:",attr_value)
#         break


#演示：控件：复选框：选中N个选项 或 获取当前选中的是哪几个选项
#选中
# name="aihao" #这一组复选框的name属性的值
# # option_values="dalanqiu,tizuqiu" #你想要选中的N个选项的value属性的值
# option_values="wanyouxi"
# eles_option=driver.find_elements_by_css_selector(f"input[type='checkbox'][name='{name}'][value]")
# for ele in eles_option:
#     attr_value=ele.get_attribute("value")
#     is_xuanzon=ele.is_selected()
#     if attr_value in option_values:#如果该选项是我想要选中的
#         if is_xuanzon:
#             pass
#         else:
#             ele.click()
#     else:#如果该选项不是我想要选中的
#         if is_xuanzon:
#             ele.click()
#         else:
#             pass

#演示：控件：下列列表：选中某选项
# ele_select=driver.find_element_by_css_selector("select[name='degree']")
# haha=Select(ele_select)
# haha.select_by_visible_text("初中/小学")


#演示：控件：多行文本框。输入数据和清空
# ele=driver.find_element_by_id("jiesao")
# ele.send_keys("你好啊，我叫张三，今年18数，\n我爱好打篮球，踢足球")

#演示：控件：日期
# js="document.getElementById('birthday').value='2000-01-01'"
# driver.execute_script(js)

#演示：控件：文件框
#方法1：
# ele=driver.find_element_by_id("zaopian")
# ele.send_keys("C:/A/1.png")
# ele.send_keys("C:/A/1.png\nC:/A/2.png")

#方法2
#selenium完成windows“打开”窗口展现
ele=driver.find_element_by_id("zaopian")
ActionChains(driver).click(ele).perform()
time.sleep(2)

#调用我们写的上传文件的autoIT脚本
#os.system(r"C:/B/uploadFiles.exe C:\A\1.png")
os.system(r'C:/B/uploadFiles.exe "C:\A\1.png" "C:\A\2.png" ')


time.sleep(5)
driver.quit()  # 关闭并退出浏览器