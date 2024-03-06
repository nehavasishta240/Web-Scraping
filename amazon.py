from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import csv


csv_header = ["Product Info", "Price", "Ratings", "No of reviews"]

# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#? without user agent I was getting captcha after multiple trials so I randomize the user agent using fake useragent

options.add_argument(f"--user-agent = {UserAgent().random}")
driver = webdriver.Chrome(options=options)
driver.get('https://www.amazon.in')

#? it waits for 5 seconds before raising an exception . if the element is not found so the element can load
#? if the element is already present then it does not wait
#? if we use sleep then it waits irrespective of weather the element is present or not

driver.implicitly_wait(5)
input_search = driver.find_element(By.ID, "twotabsearchtextbox")
search = driver.find_element(
    By.XPATH, "//input[@id = 'nav-search-submit-button']")
input_search.send_keys("Smartphones")
sleep(3)
search.click()


#? to erase the previous contents of the file
f = open('finalamazon.csv', 'w')
csvWriter = csv.writer(f)
csvWriter.writerow(csv_header)
f.close()

number_of_pages_to_scrape = 11
#? newline so that the dont have extra line between each row
with open('finalamazon.csv', 'a' , encoding='utf8' , newline="") as f:
    csvWriter = csv.writer(f)
    for i in range (number_of_pages_to_scrape):
        sleep(5)
        blocks = driver.find_elements(By.XPATH, "//div[@class = 'puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right']")
        for i in blocks:
            #? . or period before the xpath tells is to start the searching from current node 
            info = i.find_elements(
                By.XPATH, ".//span[@class = 'a-size-medium a-color-base a-text-normal']")
            price = i.find_elements(By.XPATH, ".//span[@class = 'a-price-whole']")
            ratings = i.find_elements(By.XPATH, ".//span[@class = 'a-icon-alt']")
            no_of_reviews = i.find_elements(
                By.XPATH, ".//span[@class = 'a-size-base s-underline-text']")
            # print([len(info) , len(price) , len(ratings) , len(no_of_reviews)])
            #? to prevent products who don't have ratings or price when it is unavalable comming in the csv file
            if len(info) == len(price) == len(ratings) == len(no_of_reviews) == 1:
                    csvWriter.writerow([info[0].get_attribute("innerText"), price[0].get_attribute("innerText"), ratings[0].get_attribute("innerText") , no_of_reviews[0].get_attribute("innerText")])
            # print([info[0].get_attribute("innerText"), price[0].get_attribute("innerText"), ratings[0].get_attribute("innerText") , no_of_reviews[0].get_attribute("innerText")])
        #? to go to the next page
        next_page = driver.find_element(By.LINK_TEXT, "Next")
        next_page.click()
driver.quit()
print("Done!!!!!!!!!!!!!!!")