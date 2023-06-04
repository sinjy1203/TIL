import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.firefox.options import Options

def get_gmail():
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        bot = telegram.Bot(token='')
        url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230529"
        driver.get(url)
        iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
        driver.switch_to.frame(iframe)

        title_lst = list(map(lambda x: x.text, driver.find_elements(By.XPATH, '/html/body/div/div[3]/ul/li/div/div[1]/a/strong')))
        bot.sendMessage(chat_id=6137914993, text=str(title_lst))
    except Exception as e:
        bot.sendMessage(chat_id=6137914993, text=str(e))
    driver.quit()


sched = BlockingScheduler()
sched.add_job(get_gmail, 'interval', seconds=20)
sched.start()
