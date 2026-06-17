#案例：演示隐藏元素怎么定位！
#注意：某元素能定位的前提是：该元素已经出现啦！


from selenium import webdriver  # 导入webdriver包
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com/")

#先让“搜索设置”元素出现：
ele_set=driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(ele_set).perform()

#尝试定位：隐藏元素“搜索设置”
ele_searchSet=driver.find_element(By.CSS_SELECTOR,"a.setpref.first > span.set")
ele_searchSet.click()

time.sleep(5)
driver.quit()