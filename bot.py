from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd



#data-frame#
scraped_names = []
scraped_DOC_Number = []
scraped_Supervision_County = []
scraped_Crime_Type = []
scraped_Date_Issued = []
scraped_Age = []
scraped_Birthdate = []
scraped_Height = []
scraped_Weight = []
scraped_Eye_Color = []
scraped_Hair_Color = []
scraped_Race = []
scraped_Hispanic = []
scraped_img = []


driver = webdriver.Chrome('/home/kali/chromedriver')

site = 'https://www.doc.wa.gov/information/warrants/default.aspx'


def getdata(site):
    driver.get(site)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    return soup

   
def scrape(soup):
    warrants = soup.find_all("li")
    for warrent in warrants:
        if "Name:" in warrent.text:
            sliced = str(warrent)[27:-6]
            #sliced = sliced.replace(",",".")
            scraped_names.append(sliced)

        if "DOC Number:" in warrent.text:
            sliced = str(warrent)[33:-5]
            scraped_DOC_Number.append(sliced)

        if "Supervision County:" in warrent.text:
            sliced = str(warrent)[41:-5]
            scraped_Supervision_County.append(sliced)
        
        if "Crime Type:" in warrent.text:
            sliced = str(warrent)[33:-5]
            scraped_Crime_Type.append(sliced)

        if "Date Issued:" in warrent.text:
            sliced = str(warrent)[34:-5]
            scraped_Date_Issued.append(sliced)

        if "Age:" in warrent.text:
            sliced = str(warrent)[26:-5]
            scraped_Age.append(sliced)
        
        if "Birthdate:" in warrent.text:
            sliced = str(warrent)[33:-5]
            scraped_Birthdate.append(sliced)

        if "Height:" in warrent.text:
            sliced = str(warrent)[29:-5]
            scraped_Height.append(sliced)

        if "Weight:" in warrent.text:
            sliced = str(warrent)[29:-5]
            scraped_Weight.append(sliced)

        if "Eye Color:" in warrent.text:
            sliced = str(warrent)[32:-5]
            scraped_Eye_Color.append(sliced)

        if "Hair Color:" in warrent.text:
            sliced = str(warrent)[33:-5]
            scraped_Hair_Color.append(sliced)

        if "Race:" in warrent.text:
            sliced = str(warrent)[27:-5]
            scraped_Race.append(sliced)

        if "Hispanic:" in warrent.text:
            sliced = str(warrent)[31:-5]
            scraped_Hispanic.append(sliced)

#set actual scrape for how many pages#
last_page = 250

for i in range(last_page):
    print(i)
    soup = getdata(site)
    scrape(soup)
    if i == 0:
        driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/a").click()  #first click#  
    if i == last_page:
        print ('last page')
    else:
         driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/a[2]").click()  #rest of clicks#
         time.sleep(5)
         
    #print("Step 4")


driver.quit()


'''This is the data frame from pandas. It takes the strings at the very top and turins it into a dictionary'''

data = pd.DataFrame({'Names': scraped_names,
        'DOC Number': scraped_DOC_Number,
        'Sup County': scraped_Supervision_County,
        'Crime': scraped_Crime_Type,
        'Date Issued': scraped_Date_Issued,
        'age': scraped_Age,
        'Birthdate': scraped_Birthdate,
        'Hight': scraped_Height,
        'Weight': scraped_Weight,
        'Eye Color': scraped_Eye_Color,
        'Hair Color': scraped_Hair_Color,
        'Race': scraped_Race,
        'Hispanic': scraped_Hispanic,
        })




data.to_csv('Scraped')



