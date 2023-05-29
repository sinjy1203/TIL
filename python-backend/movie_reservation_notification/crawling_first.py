import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Users/sinjy/VScodeProjects/TIL/web_crawling/chromedriver.exe')
driver.get("http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230529")

iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
driver.switch_to.frame(iframe)

day_lst = driver.find_elements(By.XPATH, '//*[@id="slider"]/div[1]/ul/li/div/a')
for day in day_lst:
    if day.find_element(By.TAG_NAME, 'span').text == "05월" and day.find_element(By.TAG_NAME, 'strong').text == "29":
        day.click()
        break


# for element in driver.find_elements(By.XPATH, '/html/body/div/div[3]/ul/li/div/div[1]/a/strong'):
#     print(element.text.strip())

# for imax in driver.find_elements(By.XPATH, '//*[@class="imax"]'):
#     print(imax.ancestor)

movie_imax_lst = driver.find_elements(By.XPATH, '/html/body/div/div[3]/ul/li[descendant::*[@class="imax"]]/div/div[1]/a/strong')

if movie_imax_lst:
    print(' '.join(map(lambda x: x.text, movie_imax_lst)), ' IMAX 예매가 열렸습니다.')
else:
    print('IMAX 예매가 아직 열리지 않았습니다.')