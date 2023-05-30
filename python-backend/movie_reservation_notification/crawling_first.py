import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('window-size=1400,1500')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('start-maximized')
# options.add_argument('enable-automation')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('user-agent={0}'.format(user_agent))
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


bot = telegram.Bot(token='5900184100:AAHwtH_6wRuJv9goEyuM8RdzA_1SCGXs2ow')


driver = webdriver.Chrome('C:/Users/sinjy/VScodeProjects/TIL/web_crawling/chromedriver.exe')
driver.get("http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230529")

iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
driver.switch_to.frame(iframe)

day_lst = driver.find_elements(By.XPATH, '//*[@id="slider"]/div[1]/ul/li/div/a')
for day in day_lst:
    if day.find_element(By.TAG_NAME, 'span').text == "05월" and day.find_element(By.TAG_NAME, 'strong').text == "30":
        day.click()
        break


def crawling_sending():
    try:
        global driver
        driver.refresh()
        iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
        driver.switch_to.frame(iframe)
        movie_imax_lst = driver.find_elements(By.XPATH, '/html/body/div/div[3]/ul/li[descendant::*[@class="imax"]]/div/div[1]/a/strong')

        if movie_imax_lst:
            bot.sendMessage(chat_id=6137914993, text=' '.join(map(lambda x: x.text, movie_imax_lst)) + ' IMAX 예매가 열렸습니다.')
    except selenium.common.exceptions.NoSuchWindowException as e:
        bot.sendMessage(chat_id=6137914993, text=str(e))
        driver = webdriver.Chrome('C:/Users/sinjy/VScodeProjects/TIL/web_crawling/chromedriver.exe', chrome_options=options)
        driver.get("http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230529")

        iframe = driver.find_element(By.XPATH, '//*[@id="ifrm_movie_time_table"]')
        driver.switch_to.frame(iframe)

        day_lst = driver.find_elements(By.XPATH, '//*[@id="slider"]/div[1]/ul/li/div/a')
        for day in day_lst:
            if day.find_element(By.TAG_NAME, 'span').text == "05월" and day.find_element(By.TAG_NAME, 'strong').text == "30":
                day.click()
                break
    except Exception as e:
        bot.sendMessage(chat_id=6137914993, text=str(e))
  
sched = BlockingScheduler()
sched.add_job(crawling_sending, 'interval', seconds=5)
sched.start()