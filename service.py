from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.chrome.options import Options

# Метод для удаления скриншотов
def del_screens(chat_id):
    os.remove(f'photo/photo{chat_id}.jpg')
    os.remove(f'photo/page_screen{chat_id}.png')


# Метод для получения ссылки на скриншот
def get_screen_link(chat_id):
    chat_id = chat_id
    files = {
        'file': open(f'photo/page_screen{chat_id}.png', 'rb'),
    }
    response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
    s = response.json()
    ss = s['data']['url']
    link = 'https://tmpfiles.org/dl/' + ss[21:]
    return link

# Метод для получения ссылки на отправленную картинку
def get_link_upload(chat_id):
    chat_id = chat_id
    files = {
        'file': open(f'photo/photo{chat_id}.jpg', 'rb'),
    }
    response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
    s = response.json()
    ss = s['data']['url']
    link = 'https://tmpfiles.org/dl/' + ss[21:]
    return link

# Метод для получения списка ссылок из яндекса
def get_links_list(chat_id):
    chat_id = chat_id
    link = get_link_upload(chat_id)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://yandex.ru/images/search?source=collections&rpt=imageview&url={link}')
    time.sleep(3)
    path = f'photo/page_screen{chat_id}.png'
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    time.sleep(3)
    # driver.save_screenshot(path)  # has scrollbar
    driver.find_element(By.TAG_NAME, 'body').screenshot(path)
    link_path = '//*[@class="CbirSites-Item"]'
    fin_link = '/div[2]/a'
    block = len(driver.find_elements(By.XPATH, link_path))
    links_list = []
    for i in range(1,block + 1):
        test = driver.find_element(By.XPATH, link_path + f'[{i}]' + fin_link)
        links_list.append(test.get_attribute('href'))
    return links_list

# Метод для получения фОРМАТИРОВАННОЙ СТРОКИ СО СПИСКОМ ИЗ ЯНДЕКСА
def get_finish_list_ya(chat_id):
    chat_id = chat_id
    s = ''
    links_list = get_links_list(chat_id)
    for i in range(len(links_list)):
        s = s + f'{i + 1}. {links_list[i]}\n'
    return s

# Метод для получения списка ссылок из гугла
def get_links_list_google():
    link = get_link_upload()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://lens.google.com/uploadbyurl?url={link}')
    time.sleep(5)
    path = '/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/page_screen.png'
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    driver.set_window_size(required_width, required_height)
    # driver.save_screenshot(path)  # has scrollbar
    driver.find_element(By.TAG_NAME, 'body').screenshot(path)
    """link_path = '//*[@class="CbirSites-Item"]'
    fin_link = '/div[2]/a'
    block = len(driver.find_elements(By.XPATH, link_path))
    links_list = []
    for i in range(1,block + 1):
        test = driver.find_element(By.XPATH, link_path + f'[{i}]' + fin_link)
        links_list.append(test.get_attribute('href'))
    return links_list"""
    return 'screen'


