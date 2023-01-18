from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By



with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
    driver.get('http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/HackTown.html')
    # time.sleep(1)

    Title = []
    date = []
    main_content=[]
    courses_offered = []
    Link = []
    
    # Title.append(driver.title)
    # dates = driver.find_elements(By.XPATH,"//div[@class='inbox']/center/center/font/b")
    # date.append(dates)
    # main_cont = driver.find_elements(By.XPATH,"//section[@id='Main']/p/font[1]/b")
    # main_content.append(main_cont)
    # data = driver.find_elements(By.XPATH,"//div[@class='inbox']")
    for i in range(1,4):
        dates = driver.find_element(By.XPATH,"//div[@class='inbox']/center/center/font/b")
        date.append(dates.text)
        title = driver.title
        Title.append(title)
        courses = driver.find_element(By.XPATH,"//div[@class='inbox']/font/b["+str(i)+"]/font")
        courses_offered.append(courses.text)

        links = driver.find_element(By.XPATH,"//div[@class='inbox']/font/a["+str(i)+"]")
        links = links.get_attribute('href')
        Link.append(links)

    driver.close()

    df = pd.DataFrame({'Title': Title, 'Last Update': date, 'Courses Offered': courses_offered, 'Links': Link})
    df.to_csv('/home/ayushlath/Web Scrapping/hacktown.csv',index=False)
    print(df)