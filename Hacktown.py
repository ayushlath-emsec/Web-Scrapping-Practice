from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By



with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
    driver.get('http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/HackTown.html')
    # time.sleep(1)

    Title = []
    body = []
    Link = []
    created_by = []
    created_at = []
    
    
    for i in range(1,4):
        dates = driver.find_element(By.XPATH,"//div[@class='inbox']/center/center/font/b")
        body.append(dates.text)
        title = driver.title
        Title.append(title)
        courses = driver.find_element(By.XPATH,"//div[@class='inbox']/font/b["+str(i)+"]/font")
        body.append(courses.text)

        links = driver.find_element(By.XPATH,"//div[@class='inbox']/font/a["+str(i)+"]")
        links = links.get_attribute('href')
        Link.append(links)
        created_at.append("29/12/2022")
        created_by.append("Ayush")

    driver.close()

    df = pd.DataFrame({'title': Title, 'body': body, 'Links': Link, 'created_at' : created_at, 'created_by' : created_by})
    df.to_csv('/home/ayushlath/Web Scrapping/hacktown.csv',index=False)
    print(df)