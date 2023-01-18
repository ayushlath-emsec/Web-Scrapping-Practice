import schedule
import time
from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


to_scrap = ["http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/HackTown.html","http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion","http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/"]
status = [0,0,0]
urgent = [0,1,0]
link_to_scrap = ""


def scrap_bianlian(link_to_scrap):
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
                driver.get(link_to_scrap)
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
    df.to_csv('/home/ayushlath/Web Scrapping 1/bianlian.csv',index=False)
    print(df)

    return "complete"


def scrap_Hacktown(link_to_scrap):
    with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
        driver.get(link_to_scrap)
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
    df.to_csv('/home/ayushlath/Web Scrapping 1/hacktown.csv',index=False)
    print(df)


    return "complete"


def scrap_cuba(link_to_scrap):

    with TorBrowserDriver("/home/ayushlath/Downloads/tor-browser") as driver:
        driver.get(link_to_scrap)
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
    df.to_csv('/home/ayushlath/Web Scrapping 1/cuba.csv',index=False)
    print(df)


    return "complete"


if len(to_scrap)!=0:
    for i in range(len(to_scrap)):
        if urgent[i]==1:
            if i==0:
                link_to_scrap = to_scrap[i]
                schedule.every(5).minutes.do(scrap_Hacktown(link_to_scrap))
                status[i] = 1

            elif i==1:
                link_to_scrap = to_scrap[i]
                schedule.every(5).minutes.do(scrap_bianlian(link_to_scrap))
                status[i] = 1
                
            else:
                link_to_scrap = to_scrap[i]
                schedule.every(5).minutes.do(scrap_cuba(link_to_scrap))
                status[i] = 1

    for j in range(len(to_scrap)):
        if status[j]==0:
            if j==0:
                link_to_scrap = to_scrap[j]
                schedule.every(5).minutes.do(scrap_Hacktown(link_to_scrap))

            elif j==1:
                link_to_scrap = to_scrap[j]
                schedule.every(5).minutes.do(scrap_bianlian(link_to_scrap))

            else:
                link_to_scrap = to_scrap[j]
                schedule.every(5).minutes.do(scrap_cuba(link_to_scrap))


while True:
    schedule.run_pending()
    time.sleep(2)