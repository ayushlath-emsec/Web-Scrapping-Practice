from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By



with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
    Links = []
    title = []
    body = []
    url = []
    pubdate = []
    created_at = []
    created_by = []
    for i in range(1,8):
        if i>1:
            driver.get("http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion/page/"+str(i)+"/")
        else:
            driver.get("http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion")
        for j in range(1,11):
            temp1 = driver.find_element(By.XPATH,"//main[@class='list']/section["+str(j)+"]/a")
            temp1 = temp1.get_attribute('href')
            Links.append(temp1)

        
        for link in Links:
            driver.get(link)
            data = driver.find_elements(By.XPATH,"//div[@class='content']/main/article")
            for d in data:
                temp2 = d.find_element(By.XPATH,"./div/h1")
                title.append(temp2.text)

                try:
                    temp4 = d.find_element(By.XPATH,"./section/p[1]/a")
                    temp4 = temp4.get_attribute('href')
                    url.append(temp4)
                except:
                    url.append("Not Found")
                stri = ""
                cnt = driver.find_elements(By.XPATH,"//div[@class='content']/main/article/section/p")
                for k in range(2,(len(cnt))+1):
                    temp3 = d.find_element(By.XPATH,"./section/p["+str(k)+"]")
                    stri = stri + (temp3.text)
                body.append(stri)

                pubdate.append("Not Found")
                created_at.append("29/12/2022")
                created_by.append("Ayush")

    driver.close()

    df = pd.DataFrame({'title': title, 'body': body,'url':url, 'pubdate': pubdate, 'created_at': created_at , 'created_by':created_by})
    df.to_csv('/home/ayushlath/Web Scrapping/bianlian.csv',index=False)
    print(df)



