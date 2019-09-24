from selenium import webdriver
import time
import re

from spiders_script import link_mysql

option = webdriver.ChromeOptions()
option.add_argument('headless')
# driver = webdriver.Chrome('./chromedriver')  # 有头打开
driver = webdriver.Chrome('./chromedriver',chrome_options=option)  #无头打开

result_list = []

def get_detils(ListA):
    # 获取当前窗口
    handle = driver.current_window_handle

    for L in ListA:
        L.click()
        # 获取所有窗口
        handles = driver.window_handles
        for newhandle in handles:
            if newhandle != handle:
                driver.switch_to.window(newhandle)

                title = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/h4').text
                time = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/div/p[1]').text
                site = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/div/p[2]').text
                site_details = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/div/p[3]').text
                introduce = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[2]/div/div').text

                time = re.sub('.*：', '', time)
                time = re.sub('[(]周\S[)]', '', time)
                site = re.sub('.*：', '', site)+re.sub('.*：', '', site_details)

                result_list.append([title,time,site,introduce])

                driver.close()
                driver.switch_to.window(handles[0])

if __name__ == '__main__':
    url = 'https://zhaopin.baidu.com/xjh?query=&curtime_extend=1567737862_1572921862&city=%E9%95%BF%E6%B2%99'
    driver.get(url)
    ListA = driver.find_elements_by_xpath('//*[@id="qz-list-box"]/div')

    for i in range(0,5):
        # 宣讲会List
        get_detils(ListA)
        driver.find_element_by_xpath('/html/body/div/div/div[4]/div[3]/div[1]/div[3]/span[8]').click()
        # 宣讲会List
        ListA = driver.find_elements_by_xpath('//*[@id="qz-list-box"]/div')
        time.sleep(1)

    print(len(result_list))
    print(result_list)
    link_mysql.insert_inf(result_list)

