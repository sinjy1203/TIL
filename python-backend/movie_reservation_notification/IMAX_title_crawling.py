import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def get_gmail():    
    try:        
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        bot = telegram.Bot(token='')
        url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230601"
        driver.get(url)

        iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
        driver.switch_to.frame(iframe)

        day_lst = driver.find_elements(By.XPATH, '//*[@id="slider"]/div[1]/ul/li/div/a')
        for day in day_lst:
            if day.find_element(By.TAG_NAME, 'span').text == "06월" and day.find_element(By.TAG_NAME, 'strong').text == "03":
                day.click()
                break
        movie_imax_lst = driver.find_elements(By.XPATH, '/html/body/div/div[3]/ul/li[descendant::*[@class="imax"]]/div/div[1]/a/strong') 

        if movie_imax_lst:
            bot.sendMessage(chat_id=6137914993, text=' '.join(map(lambda x: x.text, movie_imax_lst)) + ' IMAX 예매가 열렸습니다.')
    except Exception as e:
        bot.sendMessage(chat_id=6137914993, text=str(e))
    driver.quit()


sched = BlockingScheduler()
sched.add_job(get_gmail, 'interval', seconds=20)
sched.start()
