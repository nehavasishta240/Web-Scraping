from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import csv 

csv_header =["Mobile_name","info","Price", "Ratings","No of reviews"]

options =webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get('https://www.flipkart.com')

driver.implicitly_wait(5)
input_search =driver.find_element(By.CLASS_NAME, 'Pke_EE' )
input_search.send_keys("smartphones")
login_close=driver.find_element(By.CLASS_NAME, '_30XB9F')
login_close.click()
search=driver.find_element(By.CLASS_NAME, '_2iLD__')
sleep(3)
search.click()

 
f=open('flipkart.csv','w')
csvwriter=csv.writer(f)
csvwriter.writerow(csv_header)
f.close()

number_of_pages_to_scrape = 11

with open('flipkart.csv','a', encoding='utf8', newline="") as f:
    csvwriter=csv.writer(f)
    for i in range(number_of_pages_to_scrape):
        sleep(5) 
            
        Mobile_name=driver.find_elements(By.CLASS_NAME, '_4rR01T')
        list_of_info= driver.find_elements(By.CLASS_NAME, '_1xgFaf')
        input=[]
        for i in list_of_info:
            info=i.find_elements(By.CLASS_NAME, 'rgWa7D')
            s=""
            for j in info:
                s=s+j.text
            input.append(s)    
          
            
        Price_info=driver.find_elements(By.CLASS_NAME, '_30jeq3._1_WHN1')
        Ratings=driver.find_elements(By.CLASS_NAME, '_3LWZlK')
        N0_of_Ratings_n_reviews=driver.find_elements(By.CLASS_NAME, '_2_R_DZ' )
        
        for i in range(len(N0_of_Ratings_n_reviews)):
            csvwriter.writerow([Mobile_name[i].text ,input[i], Price_info[i].text , Ratings[i].text , N0_of_Ratings_n_reviews[i].text])
        print(len(Mobile_name) , len(Price_info) , len(Ratings) , len(N0_of_Ratings_n_reviews))

        next = driver.find_elements(By.CLASS_NAME, '_1LKTO3')
        print(len(next))
        if len(next)>1:
            next[1].click()
        else:
            next[0].click()
        
print("DONE!!!!!!")
