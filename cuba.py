from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By



with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
    driver.get('http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/')
    # time.sleep(1)

    Title = []
    body = []
    created_at = [] 
    created_by = []
    

    
    for i in range(2,7):
        company_name = driver.find_element(By.XPATH,"//div[@class='row']/div[1]/div[1]/div["+str(i)+"]/div/div[2]/a")
        company_name = company_name.get_attribute('href')
        arr = []
        arr = company_name.split('/')
        company_name = arr[-1]
        Title.append(company_name)

        company_name = driver.find_element(By.XPATH,"//div[@class='row']/div[1]/div[1]/div["+str(i)+"]/div/div[2]/a")
        body.append(company_name.text)
        created_at.append("29/12/2022")
        created_by.append("Ayush")

    
    driver.close()

    df = pd.DataFrame({'title': Title, 'body': body, 'created_at': created_at , 'created_by':created_by})
    df.to_csv('/home/ayushlath/Web Scrapping/cuba.csv',index=False)
    print(df)




