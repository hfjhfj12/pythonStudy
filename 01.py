#案例：演示web自动化测试环境是否OK（针对：Chrome浏览器）

from selenium import webdriver  # 导入webdriver包
import time
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome(executable_path=r"E:\cesi_install\python_install\Chromedriver\chromedriver.exe")

driver = webdriver.Chrome()

driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(30)

driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点

ele_input=driver.find_element(By.ID,"kw")
ele_input.send_keys("Selenium自动化测试")

ele_baiduyixia=driver.find_element(By.ID,"su")
ele_baiduyixia.click()


time.sleep(5)
driver.quit()  # 关闭并退出浏览器

print("hello")