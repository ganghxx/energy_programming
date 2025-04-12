from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, strftime
from random import randint
from send_msg import send_push_notification as spn
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# essential information
product_url = "https://kream.co.kr/products/481547?size="
target_price = 130000
size = "255"
kream_id = "kream_id" # 본인 아이디 입력
kream_pw = "kream_pw" # 본인 비밀번호 입력

# 로그인
driver.get("https://kream.co.kr/login")
sleep(2)
driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div/form/div[1]/div/input').send_keys(kream_id)
driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div/form/div[2]/div/input').send_keys(kream_pw)
driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div/form/div[3]/button').click()
sleep(2)

while True:
    #타겟 상품 페이지로 이동
    driver.get(product_url)
    print("검색시간: ", strftime('%Y.%m.%d %H:%M:%S'))
    sleep(2)

    # 상품 정보 가져오기
    
    try:
        product_name = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p[1]').text
        driver.find_element(By.CLASS_NAME, 'detail-size').click()
        sleep(2)

        div_size_price = driver.find_elements(By.CLASS_NAME,'select_item.select_option_picker.select_option_picker_text')
        size_list = []
        price_list = []

        for i in div_size_price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'), 'html.parser')
            size_list.append(soup.find_all('p')[0].text)
            price_list.append(soup.find_all('p')[1].text)

        for i in range(len(size_list)):
            if size == size_list[i]:
                price_now = int(price_list[i].replace(",",""))

    except:
        product_name = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p[1]').text
        price_now = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/p[2]').text
        if "%" in price_now:
            price_now = price_now[4:]
            price_now = int(price_now.replace(",","")).replace("원","")
        else:
            price_now = int(price_now.replace(",","").replace("원",""))
            
    if price_now <= target_price:
        title = f"타겟 금액 달성"
        message = f"{product_name} 상품의 금액이 현재 {price_now}원으로 설정한 {target_price}원 보다 같거나 낮습니다."
        spn(title, message, product_url)
        break
    else:
        sleep(randint(300,600))