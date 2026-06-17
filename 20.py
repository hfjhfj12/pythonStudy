#案例：演示一个字节跳动的web自动化面试题！

from selenium import webdriver  # 导入webdriver包
import time

driver=webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com/")

#输入搜索关键字aria-label="字节跳动，字节跳动，百度百科"
driver.find_element_by_id("kw").send_keys("字节跳动")

#点击“百度一下”按钮
driver.find_element_by_id("su").click()
time.sleep(2)

#点击“字节跳动-百度百科”
ele1=driver.find_element_by_css_selector("a[aria-label='字节跳动，字节跳动，百度百科']")
ele1.click()

#切换到“字节跳动-百度百科”新窗口
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)

#找这些事件的父标签
ele_div=driver.find_element_by_css_selector("div.main-content.J-content")
eles=ele_div.find_elements_by_css_selector("div.para.MARK_MODULE[label-module='para'][data-uuid][data-pid]")
for x in eles:
    attr_data_pid=x.get_attribute("data-pid")
    a=int(attr_data_pid)
    if a>=5 and a<=52:
        text=x.text #"2012年3月，北京字节跳动科技有限公司成立 [5]  ；"
        b=text.split("，",1)
        sijian=b[0]
        sj=b[1]

        with open("C:/A/heihei.csv","a") as fp:
            fp.write(f"{sijian},{sj}\n")

time.sleep(5)
driver.quit()

print("hello2")