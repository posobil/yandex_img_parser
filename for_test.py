from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.chrome.options import Options


def get_link_upload():
    files = {
        'file': open('/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/photo.jpg', 'rb'),
    }
    response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
    s = response.json()
    ss = s['data']['url']
    link = 'https://tmpfiles.org/dl/' + ss[21:]
    return link

link = get_link_upload()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(f'https://lens.google.com/uploadbyurl?url={link}')
time.sleep(3)
path = '/photo/page_screen.png'
required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(required_width, required_height)
driver.set_window_size(required_width, required_height)
# driver.save_screenshot(path)  # has scrollbar
driver.find_element(By.TAG_NAME, 'body').screenshot(path)
# Visual matches
ch_str = '//*[text()="Визуальные совпадения"]'
dicts_links = '//*[@class="aah4tc"]/div'
block = len(driver.find_elements(By.XPATH, dicts_links))
print(block)
fin_link = '/div[2]/a'
time.sleep(2)
links_list = []
ll = ''
ch = 1
for i in range(1,block + 1):
    list_links = f'//*[@class="aah4tc"]/div[{i}]/div'
    print(len(driver.find_elements(By.XPATH, list_links)))
    for b in range(1, (len(driver.find_elements(By.XPATH, list_links))) + 1):
        link_page = driver.find_elements(By.XPATH, dicts_links + f'[{i}]/div[{b}]/div')
        print(link_page)
        """ll = ll + f'{ch} {link_page}'
        ch += 1

print(ll)"""