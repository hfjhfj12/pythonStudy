#案例：演示键盘操作！
'''
案例需求：注册实例.html中
    1). 输入用户名：admin1，暂停2秒 删除字符1
    2). 全选用户名：admin      暂停2秒
    3). 复制用户名：admin      暂停2秒
    4). 粘贴到密码框          暂停2秒
    5). 关闭浏览器
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

url="http://oss.52studyit.net/webzdh/zuceb.html"
driver.get(url)

ele_user=driver.find_element_by_css_selector("#userB");
ele_user.send_keys("admin1");
sleep(2)
ele_user.send_keys(Keys.BACK_SPACE) #退格键，调用一次删词一个字符！
sleep(2)
ele_user.send_keys(Keys.CONTROL,"a")#CTRL+A，全选
sleep(2)
ele_user.send_keys(Keys.CONTROL,"c")#CTRL+C，复制

ele_pwd=driver.find_element_by_css_selector("#passwordB");
ele_pwd.send_keys(Keys.CONTROL,"v")#CTRL+V，粘贴
sleep(2)
driver.quit()